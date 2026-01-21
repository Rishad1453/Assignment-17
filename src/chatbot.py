"""Main chatbot orchestration and logic"""

from typing import Optional, Tuple, List
import os

from src.faq_retriever import FAQRetriever
from src.metadata_filter import MetadataFilter
from src.response_generator import ResponseGenerator
from src.bangla_processor import BanglaProcessor


class BanglaFAQChatbot:
    """
    Main chatbot class orchestrating RAG pipeline
    
    Flow:
    1. User selects topic
    2. User asks question
    3. Filter FAQs by topic
    4. Retrieve relevant FAQs
    5. Generate response
    6. Show fallback if no match
    """

    # Confidence threshold for accepting an answer
    CONFIDENCE_THRESHOLD = 0.1  # Lower threshold for simpler matching

    def __init__(self, faq_database_path: str):
        """
        Initialize chatbot
        
        Args:
            faq_database_path: Path to FAQ JSON file
        """
        if not os.path.exists(faq_database_path):
            raise FileNotFoundError(f"FAQ database not found: {faq_database_path}")
        
        self.retriever = FAQRetriever(faq_database_path)
        self.filter = MetadataFilter()
        self.processor = BanglaProcessor()
        
        print(f"✅ चेटबट आरम्भ किया गया। {self.retriever.get_faq_count()} FAQs लोड किए गए।")

    def answer_question(
        self,
        query: str,
        topic: str,
        difficulty: Optional[str] = None,
        return_multiple: bool = False,
        top_k: int = 1
    ) -> Tuple[Optional[List], bool]:
        """
        Answer a question using RAG pipeline
        
        Args:
            query: User's question
            topic: Selected topic
            difficulty: Optional difficulty filter
            return_multiple: Whether to return multiple results
            top_k: Number of results to return
            
        Returns:
            Tuple of (results, is_fallback) where results is list of (FAQ, score)
        """
        try:
            # Step 1: Validate topic
            if not self.filter.is_valid_topic(topic):
                return None, True
            
            # Step 2: Filter FAQs by topic
            filtered_faqs = self.filter.filter_by_topic(
                self.retriever.get_all_faqs(),
                topic
            )
            
            # Step 3: Apply difficulty filter if provided
            if difficulty and self.filter.is_valid_difficulty(difficulty):
                filtered_faqs = self.filter.filter_by_difficulty(filtered_faqs, difficulty)
            
            if not filtered_faqs:
                return None, True
            
            # Step 4: Retrieve relevant FAQs
            results = self.retriever.retrieve(
                query,
                candidates=filtered_faqs,
                top_k=top_k
            )
            
            # Step 5: Check if results meet confidence threshold
            if results and results[0][1] >= self.CONFIDENCE_THRESHOLD:
                return results, False
            
            # No good match found
            return None, True
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return None, True

    def generate_answer(
        self,
        query: str,
        topic: str,
        difficulty: Optional[str] = None
    ) -> Tuple[str, bool]:
        """
        Generate complete answer for user query
        
        Args:
            query: User's question
            topic: Selected topic
            difficulty: Optional difficulty filter
            
        Returns:
            Tuple of (response_text, is_fallback)
        """
        # Get answer from RAG
        results, is_fallback = self.answer_question(
            query, topic, difficulty, return_multiple=False
        )
        
        if is_fallback or not results:
            # Return fallback response
            fallback_msg = ResponseGenerator.get_fallback_response(topic)
            return fallback_msg, True
        
        # Generate response from matched FAQ
        faq_match = results[0]
        faq, score = faq_match
        
        # Format response with metadata
        response = ResponseGenerator.format_response_with_context(
            response_text=faq.get('answer', ''),
            topic=topic,
            difficulty=faq.get('difficulty', ''),
            confidence=score,
            is_fallback=False
        )
        
        return response, False

    def get_stats(self) -> dict:
        """Get chatbot statistics"""
        stats = {
            'total_faqs': self.retriever.get_faq_count(),
            'topics': list(self.filter.get_topics().keys()),
            'difficulties': list(self.filter.get_difficulties().keys())
        }
        
        # Count FAQs per topic
        for topic in stats['topics']:
            topic_faqs = self.filter.filter_by_topic(
                self.retriever.get_all_faqs(), topic
            )
            stats[f'{topic}_count'] = len(topic_faqs)
        
        return stats

    def search_similar(self, query: str, top_k: int = 3) -> List[dict]:
        """
        Search for similar FAQs without topic filter
        
        Args:
            query: Search query
            top_k: Number of results
            
        Returns:
            List of similar FAQs
        """
        results = self.retriever.retrieve(query, top_k=top_k)
        return [faq for faq, _ in results]

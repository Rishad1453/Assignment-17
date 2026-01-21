"""Response generation from retrieved FAQs with fallback handling"""

from typing import Dict, Tuple, Optional, List


class ResponseGenerator:
    """Generate natural language responses from FAQ matches"""

    # Fallback messages for each topic
    FALLBACK_MESSAGES = {
        'শিক্ষা': 'দুঃখিত, শিক্ষা সংক্রান্ত এই প্রশ্নের উত্তর আমার কাছে নেই। অনুগ্রহ করে অন্য কিছু জিজ্ঞাসা করুন।',
        'স্বাস্থ্য': 'দুঃখিত, স্বাস্থ্য সংক্রান্ত এই প্রশ্নের উত্তর আমার কাছে নেই। একজন ডাক্তারের সাথে পরামর্শ করার পরামর্শ দিচ্ছি।',
        'ভ্রমণ': 'দুঃখিত, ভ্রমণ সংক্রান্ত এই প্রশ্নের উত্তর আমার কাছে নেই। অনুগ্রহ করে অন্য কিছু জিজ্ঞাসা করুন।',
        'প্রযুক্তি': 'দুঃখিত, প্রযুক্তি সংক্রান্ত এই প্রশ্নের উত্তর আমার কাছে নেই। অনুগ্রহ করে অন্য কিছু জিজ্ঞাসা করুন।',
        'খেলাধুলা': 'দুঃখিত, খেলাধুলা সংক্রান্ত এই প্রশ্নের উত্তর আমার কাছে নেই। অনুগ্রহ করে অন্য কিছু জিজ্ঞাসা করুন।',
    }

    GENERIC_FALLBACK = 'দুঃখিত, এই প্রশ্নের উত্তর আমার কাছে এখন নেই। অনুগ্রহ করে অন্য কিছু জিজ্ঞাসা করুন।'

    @staticmethod
    def generate_response(
        faq_match: Tuple[Dict, float],
        include_metadata: bool = True
    ) -> str:
        """
        Generate response from FAQ match
        
        Args:
            faq_match: Tuple of (FAQ dict, relevance score)
            include_metadata: Whether to include difficulty and source
            
        Returns:
            Formatted response string
        """
        faq, score = faq_match
        
        response = faq.get('answer', '')
        
        if include_metadata:
            difficulty = faq.get('difficulty', 'অজানা')
            source_q = faq.get('question', '')
            
            response += f'\n\n[প্রাসঙ্গিকতা স্তর: {difficulty} | আত্মবিশ্বাস: {score:.0%}]'
            
            if source_q:
                response += f'\n[মূল প্রশ্ন: {source_q}]'
        
        return response

    @staticmethod
    def get_fallback_response(topic: Optional[str] = None) -> str:
        """
        Get fallback response when no FAQ is found
        
        Args:
            topic: Optional topic for topic-specific fallback
            
        Returns:
            Fallback message
        """
        if topic and topic in ResponseGenerator.FALLBACK_MESSAGES:
            return ResponseGenerator.FALLBACK_MESSAGES[topic]
        
        return ResponseGenerator.GENERIC_FALLBACK

    @staticmethod
    def format_response_with_context(
        response_text: str,
        topic: str,
        difficulty: str,
        confidence: float,
        is_fallback: bool = False
    ) -> str:
        """
        Format response with full context
        
        Args:
            response_text: The answer text
            topic: Topic of the FAQ
            difficulty: Difficulty level
            confidence: Confidence score (0-1)
            is_fallback: Whether this is a fallback response
            
        Returns:
            Formatted response with context
        """
        if is_fallback:
            return response_text
        
        formatted = f"উত্তর:\n{response_text}\n"
        formatted += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        formatted += f"বিষয়: {topic} | স্তর: {difficulty} | আত্মবিশ্বাস: {confidence:.0%}"
        
        return formatted

    @staticmethod
    def generate_detailed_response(
        results: List[Tuple[Dict, float]],
        top_k: int = 3
    ) -> str:
        """
        Generate detailed response showing multiple results
        
        Args:
            results: List of (FAQ, score) tuples
            top_k: Number of results to include
            
        Returns:
            Detailed response with multiple options
        """
        if not results:
            return ResponseGenerator.GENERIC_FALLBACK
        
        response = "সম্ভাব্য উত্তরগুলি:\n\n"
        
        for idx, (faq, score) in enumerate(results[:top_k], 1):
            response += f"{idx}. প্রশ্ন: {faq.get('question', '')}\n"
            response += f"   উত্তর: {faq.get('answer', '')}\n"
            response += f"   আত্মবিশ্বাস: {score:.0%} | স্তর: {faq.get('difficulty', '')}\n\n"
        
        return response

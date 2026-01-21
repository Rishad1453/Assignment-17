"""RAG-based FAQ retriever using semantic search"""

import json
import os
from typing import List, Dict, Tuple, Optional
import numpy as np
from collections import Counter

from .bangla_processor import BanglaProcessor


class FAQRetriever:
    """Retrieve relevant FAQs using semantic search and similarity matching"""

    def __init__(self, faq_file_path: str):
        """
        Initialize FAQ retriever
        
        Args:
            faq_file_path: Path to FAQ JSON database
        """
        self.faq_file_path = faq_file_path
        self.faqs = []
        self.load_faqs()

    def load_faqs(self) -> None:
        """Load FAQ database from JSON file"""
        if not os.path.exists(self.faq_file_path):
            raise FileNotFoundError(f"FAQ file not found: {self.faq_file_path}")
        
        with open(self.faq_file_path, 'r', encoding='utf-8') as f:
            self.faqs = json.load(f)
        
        if not self.faqs:
            raise ValueError("FAQ database is empty")

    def _calculate_similarity(self, query: str, text: str) -> float:
        """
        Calculate similarity between query and text using word overlap
        
        Args:
            query: User query
            text: FAQ text (question or answer)
            
        Returns:
            Similarity score (0-1)
        """
        query_tokens = set(BanglaProcessor.tokenize(query.lower()))
        text_tokens = set(BanglaProcessor.tokenize(text.lower()))
        
        if not query_tokens or not text_tokens:
            return 0.0
        
        intersection = query_tokens & text_tokens
        union = query_tokens | text_tokens
        
        return len(intersection) / len(union) if union else 0.0

    def _rank_results(self, query: str, candidates: List[Dict]) -> List[Tuple[Dict, float]]:
        """
        Rank FAQ candidates by relevance to query
        
        Args:
            query: User query
            candidates: List of candidate FAQs
            
        Returns:
            List of (FAQ, score) tuples sorted by score (descending)
        """
        results = []
        
        for faq in candidates:
            question_sim = self._calculate_similarity(query, faq.get('question', ''))
            keyword_score = 0
            for keyword in faq.get('keywords', []):
                if keyword.lower() in query.lower():
                    keyword_score += 0.3
            
            total_score = (question_sim * 0.7) + min(keyword_score, 0.3)
            results.append((faq, total_score))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def retrieve(
        self,
        query: str,
        candidates: Optional[List[Dict]] = None,
        top_k: int = 1
    ) -> List[Tuple[Dict, float]]:
        """
        Retrieve top-k most relevant FAQs for a query
        
        Args:
            query: User question/query
            candidates: Optional list of pre-filtered FAQs to search within
            top_k: Number of top results to return
            
        Returns:
            List of (FAQ, score) tuples
        """
        search_space = candidates if candidates else self.faqs
        if not search_space:
            return []
        
        ranked = self._rank_results(query, search_space)
        return ranked[:top_k]

    def get_faq_by_id(self, faq_id: str) -> Optional[Dict]:
        """Get FAQ by its ID"""
        for faq in self.faqs:
            if faq.get('id') == faq_id:
                return faq
        return None

    def get_all_faqs(self) -> List[Dict]:
        """Get all FAQs"""
        return self.faqs.copy()

    def get_faq_count(self) -> int:
        """Get total number of FAQs"""
        return len(self.faqs)

    def search_by_keywords(self, keywords: List[str]) -> List[Dict]:
        """Search FAQs by list of keywords"""
        results = []
        
        for faq in self.faqs:
            faq_keywords = set(faq.get('keywords', []))
            if any(kw in faq_keywords for kw in keywords):
                results.append(faq)
        
        return results

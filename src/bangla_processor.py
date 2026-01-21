"""Bangla text processing module for normalization and preprocessing"""

import re
import unicodedata
from typing import List, Set


class BanglaProcessor:
    """Handle Bangla text processing, normalization, and tokenization"""

    BANGLA_SCRIPT_RANGE = (0x0980, 0x09FF)
    
    STOP_WORDS = {
        'এ', 'এর', 'অন', 'একটি', 'কোন', 'কিছু', 'যা', 'যে', 'যদি', 'তবে',
        'এবং', 'কিংবা', 'অথবা', 'না', 'নয়', 'সঙ্গে', 'থেকে', 'পর্যন্ত',
        'সাথে', 'মধ্যে', 'জন্য', 'দ্বারা', 'দ্বারার', 'করে', 'করা', 'করেন',
        'হয়', 'হয়েছে', 'হবে', 'আছে', 'আছেন', 'ছিল', 'ছিলেন', 'আছিল',
        'আমি', 'আপনি', 'তিনি', 'সে', 'আমরা', 'তারা', 'এটি', 'এগুলি'
    }

    def __init__(self):
        """Initialize Bangla processor"""
        pass

    @staticmethod
    def is_bangla(char: str) -> bool:
        """Check if character is Bangla"""
        code = ord(char)
        return BanglaProcessor.BANGLA_SCRIPT_RANGE[0] <= code <= BanglaProcessor.BANGLA_SCRIPT_RANGE[1]

    @staticmethod
    def normalize(text: str) -> str:
        """Normalize Bangla text by handling diacritics and common variations"""
        if not text:
            return text
        
        text = unicodedata.normalize('NFD', text)
        text = ''.join(
            char for char in text 
            if not unicodedata.combining(char)
        )
        text = unicodedata.normalize('NFC', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text

    @staticmethod
    def tokenize(text: str) -> List[str]:
        """Tokenize Bangla text into words"""
        # Normalize first
        text = BanglaProcessor.normalize(text)
        
        # Split by whitespace and punctuation
        tokens = re.findall(r'\b\w+\b', text, re.UNICODE)
        
        return tokens

    @staticmethod
    def remove_stopwords(tokens: List[str]) -> List[str]:
        """Remove common Bangla stop words"""
        return [token for token in tokens if token.lower() not in BanglaProcessor.STOP_WORDS]

    @staticmethod
    def extract_keywords(text: str, top_n: int = 5) -> List[str]:
        """Extract keywords from Bangla text"""
        tokens = BanglaProcessor.tokenize(text)
        tokens = BanglaProcessor.remove_stopwords(tokens)
        
        # Return top tokens (simple frequency-based)
        from collections import Counter
        freq = Counter(tokens)
        
        keywords = [word for word, _ in freq.most_common(top_n)]
        return keywords

    @staticmethod
    def preprocess(text: str) -> List[str]:
        """Full preprocessing pipeline"""
        text = BanglaProcessor.normalize(text)
        tokens = BanglaProcessor.tokenize(text)
        tokens = BanglaProcessor.remove_stopwords(tokens)
        return tokens

    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """Calculate simple word overlap similarity between two Bangla texts"""
        tokens1 = set(BanglaProcessor.tokenize(text1.lower()))
        tokens2 = set(BanglaProcessor.tokenize(text2.lower()))
        
        if not tokens1 or not tokens2:
            return 0.0
        
        intersection = tokens1 & tokens2
        union = tokens1 | tokens2
        
        # Jaccard similarity
        return len(intersection) / len(union) if union else 0.0

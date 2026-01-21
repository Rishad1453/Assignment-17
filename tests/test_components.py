"""Unit tests for Bangla FAQ Chatbot components"""

import unittest
import os
import json
from src.bangla_processor import BanglaProcessor
from src.metadata_filter import MetadataFilter
from src.faq_retriever import FAQRetriever
from src.chatbot import BanglaFAQChatbot


class TestBanglaProcessor(unittest.TestCase):
    """Test Bangla text processing"""
    
    def test_normalize(self):
        """Test text normalization"""
        text = "বাংলা   পাঠ"
        normalized = BanglaProcessor.normalize(text)
        self.assertEqual(normalized, "বাংলা পাঠ")
    
    def test_tokenize(self):
        """Test tokenization"""
        text = "বাংলা ভাষা খুবই সুন্দর"
        tokens = BanglaProcessor.tokenize(text)
        self.assertGreater(len(tokens), 0)
        self.assertIn("বাংলা", tokens)
    
    def test_is_bangla(self):
        """Test Bangla character detection"""
        self.assertTrue(BanglaProcessor.is_bangla('ব'))
        self.assertTrue(BanglaProcessor.is_bangla('আ'))
        self.assertFalse(BanglaProcessor.is_bangla('a'))


class TestMetadataFilter(unittest.TestCase):
    """Test metadata filtering"""
    
    def setUp(self):
        """Set up test data"""
        self.sample_faqs = [
            {
                'id': 'test_1',
                'topic': 'শিক্ষা',
                'difficulty': 'সহজ',
                'question': 'প্রশ্ন ১',
                'answer': 'উত্তর ১'
            },
            {
                'id': 'test_2',
                'topic': 'স্বাস্থ্য',
                'difficulty': 'মাঝারি',
                'question': 'প্রশ্ন ২',
                'answer': 'উত্তর ২'
            }
        ]
    
    def test_filter_by_topic(self):
        """Test topic filtering"""
        filtered = MetadataFilter.filter_by_topic(self.sample_faqs, 'শিক্ষা')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['id'], 'test_1')
    
    def test_valid_topic(self):
        """Test topic validation"""
        self.assertTrue(MetadataFilter.is_valid_topic('শিক্ষা'))
        self.assertFalse(MetadataFilter.is_valid_topic('অবৈধ_বিষয়'))
    
    def test_valid_difficulty(self):
        """Test difficulty validation"""
        self.assertTrue(MetadataFilter.is_valid_difficulty('সহজ'))
        self.assertFalse(MetadataFilter.is_valid_difficulty('অবৈধ'))


class TestFAQRetriever(unittest.TestCase):
    """Test FAQ retrieval"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test FAQ file"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cls.faq_path = os.path.join(script_dir, 'data', 'bangla_faqs.json')
    
    def test_load_faqs(self):
        """Test FAQ loading"""
        if os.path.exists(self.faq_path):
            retriever = FAQRetriever(self.faq_path)
            self.assertGreater(retriever.get_faq_count(), 0)
    
    def test_retrieve(self):
        """Test FAQ retrieval"""
        if os.path.exists(self.faq_path):
            retriever = FAQRetriever(self.faq_path)
            results = retriever.retrieve("পড়াশোনা", top_k=1)
            self.assertIsInstance(results, list)


class TestChatbot(unittest.TestCase):
    """Test main chatbot"""
    
    @classmethod
    def setUpClass(cls):
        """Set up chatbot"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cls.faq_path = os.path.join(script_dir, 'data', 'bangla_faqs.json')
    
    def test_chatbot_initialization(self):
        """Test chatbot initialization"""
        if os.path.exists(self.faq_path):
            try:
                chatbot = BanglaFAQChatbot(self.faq_path)
                self.assertIsNotNone(chatbot)
            except FileNotFoundError:
                self.skipTest("FAQ file not found")
    
    def test_answer_generation(self):
        """Test answer generation"""
        if os.path.exists(self.faq_path):
            try:
                chatbot = BanglaFAQChatbot(self.faq_path)
                response, is_fallback = chatbot.generate_answer(
                    "পড়াশোনা", "শিক্ষা"
                )
                self.assertIsNotNone(response)
                self.assertIsInstance(is_fallback, bool)
            except FileNotFoundError:
                self.skipTest("FAQ file not found")


if __name__ == '__main__':
    unittest.main()

"""Metadata filtering for FAQs based on topic and difficulty"""

from typing import List, Dict, Optional


class MetadataFilter:
    """Filter FAQs by metadata (topic, difficulty)"""

    VALID_TOPICS = {
        'শিক্ষা': 'Education',
        'স্বাস্থ্য': 'Health',
        'ভ্রমণ': 'Travel',
        'প্রযুক্তি': 'Technology',
        'খেলাধুলা': 'Sports'
    }

    VALID_DIFFICULTY = {
        'সহজ': 'Easy',
        'মাঝারি': 'Medium',
        'কঠিন': 'Hard'
    }

    @staticmethod
    def is_valid_topic(topic: str) -> bool:
        """Check if topic is valid"""
        return topic in MetadataFilter.VALID_TOPICS

    @staticmethod
    def is_valid_difficulty(difficulty: str) -> bool:
        """Check if difficulty level is valid"""
        return difficulty in MetadataFilter.VALID_DIFFICULTY

    @staticmethod
    def filter_by_topic(faqs: List[Dict], topic: str) -> List[Dict]:
        """Filter FAQs by specific topic"""
        if not MetadataFilter.is_valid_topic(topic):
            raise ValueError(f"Invalid topic: {topic}")
        
        return [faq for faq in faqs if faq.get('topic') == topic]

    @staticmethod
    def filter_by_difficulty(faqs: List[Dict], difficulty: str) -> List[Dict]:
        """Filter FAQs by difficulty level"""
        if not MetadataFilter.is_valid_difficulty(difficulty):
            raise ValueError(f"Invalid difficulty: {difficulty}")
        
        return [faq for faq in faqs if faq.get('difficulty') == difficulty]

    @staticmethod
    def apply_filters(
        faqs: List[Dict],
        topic: Optional[str] = None,
        difficulty: Optional[str] = None
    ) -> List[Dict]:
        """Apply multiple filters to FAQs"""
        filtered = faqs
        
        if topic:
            filtered = MetadataFilter.filter_by_topic(filtered, topic)
        
        if difficulty:
            filtered = MetadataFilter.filter_by_difficulty(filtered, difficulty)
        
        return filtered

    @staticmethod
    def get_topics() -> Dict[str, str]:
        """Get all available topics"""
        return MetadataFilter.VALID_TOPICS.copy()

    @staticmethod
    def get_difficulties() -> Dict[str, str]:
        """Get all available difficulty levels"""
        return MetadataFilter.VALID_DIFFICULTY.copy()

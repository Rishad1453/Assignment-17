"""Console-based user interface for Bangla FAQ chatbot"""

from typing import Optional
from src.metadata_filter import MetadataFilter


class ConsoleUI:
    """Handle console-based menu and user interaction"""

    MENU_HEADER = """
╔════════════════════════════════════════════════════════╗
║           বাংলা FAQ চ্যাটবট স্বাগতম             ║
║     Bangla FAQ Chatbot - RAG Based System             ║
╚════════════════════════════════════════════════════════╝
"""

    TOPIC_MENU = """
╔════════════════════════════════════════════════════════╗
║            বিষয় নির্বাচন করুন (Select Topic)        ║
╚════════════════════════════════════════════════════════╝

1. 📚 শিক্ষা (Education)
2. 🏥 স্বাস্থ্য (Health)
3. ✈️  ভ্রমণ (Travel)
4. 💻 প্রযুক্তি (Technology)
5. ⚽ খেলাধুলা (Sports)
0. 🚪 বের হন (Exit)

>>> আপনার পছন্দ (Your Choice): """

    DIFFICULTY_MENU = """
╔════════════════════════════════════════════════════════╗
║      কঠিনতা স্তর নির্বাচন করুন (Optional)          ║
║          (Difficulty Level - Optional)                ║
╚════════════════════════════════════════════════════════╝

1. সহজ (Easy)
2. মাঝারি (Medium)
3. কঠিন (Hard)
0. সব স্তর (All Levels)

>>> আপনার পছন্দ (Your Choice): """

    def __init__(self):
        """Initialize console UI"""
        self.topics_map = {
            '1': 'শিক্ষা',
            '2': 'স্বাস্থ্য',
            '3': 'ভ্রমণ',
            '4': 'প্রযুক্তি',
            '5': 'খেলাধুলা'
        }
        
        self.difficulty_map = {
            '1': 'সহজ',
            '2': 'মাঝারি',
            '3': 'কঠিন',
            '0': None
        }

    def display_header(self) -> None:
        """Display welcome header"""
        print(self.MENU_HEADER)

    def display_menu(self) -> Optional[str]:
        """
        Display topic selection menu
        
        Returns:
            Selected topic in Bangla or None for exit
        """
        print(self.TOPIC_MENU, end='')
        choice = input().strip()
        
        if choice == '0':
            return None
        
        if choice in self.topics_map:
            return self.topics_map[choice]
        
        print("❌ অবৈধ নির্বাচন। অনুগ্রহ করে আবার চেষ্টা করুন।")
        return self.display_menu()

    def display_difficulty_menu(self) -> Optional[str]:
        """
        Display difficulty level selection menu
        
        Returns:
            Selected difficulty level or None for all
        """
        print(self.DIFFICULTY_MENU, end='')
        choice = input().strip()
        
        if choice in self.difficulty_map:
            return self.difficulty_map[choice]
        
        print("❌ অবৈধ নির্বাচন। অনুগ্রহ করে আবার চেষ্টা করুন।")
        return self.display_difficulty_menu()

    def get_user_query(self, topic: str) -> str:
        """
        Get user's question for selected topic
        
        Args:
            topic: Selected topic in Bangla
            
        Returns:
            User's question
        """
        print(f"\n╔════════════════════════════════════════════════════════╗")
        print(f"║ বিষয়: {topic:20} (Topic: {MetadataFilter.VALID_TOPICS.get(topic, 'Unknown')})")
        print(f"╚════════════════════════════════════════════════════════╝\n")
        
        query = input(">>> আপনার প্রশ্ন (Your Question): ").strip()
        
        if not query:
            print("❌ অনুগ্রহ করে একটি প্রশ্ন লিখুন।")
            return self.get_user_query(topic)
        
        return query

    def display_response(self, response: str, is_fallback: bool = False) -> None:
        """
        Display response to user
        
        Args:
            response: Response text to display
            is_fallback: Whether this is a fallback response
        """
        if is_fallback:
            print(f"\n⚠️  ফলব্যাক প্রতিক্রিয়া (Fallback Response):")
        else:
            print(f"\n✅ প্রাসঙ্গিক উত্তর পাওয়া গেছে:")
        
        print(f"\n{response}\n")

    def ask_continue(self) -> bool:
        """
        Ask user if they want to continue
        
        Returns:
            True to continue, False to exit
        """
        print("─" * 54)
        response = input("\n>>> আরও প্রশ্ন? (Continue?) (হ্যাঁ/না / Yes/No): ").strip().lower()
        
        if response in ['হ্যাঁ', 'yes', 'y', 'জি', 'হ', 'ঠিক আছে']:
            return True
        
        return False

    def display_goodbye(self) -> None:
        """Display goodbye message"""
        print("""
╔════════════════════════════════════════════════════════╗
║                                                        ║
║  ধন্যবাদ! আমাদের সাথে থাকার জন্য ধন্যবাদ।         ║
║     Thank you for using Bangla FAQ Chatbot!           ║
║                                                        ║
║  পুনরায় দেখা হবে! (See you again!)                  ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
""")

    def display_error(self, error_msg: str) -> None:
        """Display error message"""
        print(f"\n❌ ত্রুটি (Error): {error_msg}\n")

    def display_loading(self) -> None:
        """Display loading message"""
        print("\n⏳ প্রক্রিয়াজাত করা হচ্ছে... (Processing...)\n")

    @staticmethod
    def clear_screen() -> None:
        """Clear console screen"""
        import os
        os.system('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def print_divider(char: str = '─', length: int = 54) -> None:
        """Print a divider line"""
        print(char * length)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main entry point for Bangla FAQ Chatbot"""

import os
import sys

from src.chatbot import BanglaFAQChatbot
from console_ui import ConsoleUI


def main():
    """Main application loop"""
    
    # Determine FAQ database path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    faq_path = os.path.join(script_dir, 'data', 'bangla_faqs.json')
    
    # Initialize chatbot and UI
    try:
        chatbot = BanglaFAQChatbot(faq_path)
        ui = ConsoleUI()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    # Main loop
    ui.display_header()
    
    while True:
        # Get topic from user
        topic = ui.display_menu()
        
        if topic is None:
            # User chose to exit
            ui.display_goodbye()
            break
        
        # Get difficulty filter (optional)
        difficulty = ui.display_difficulty_menu()
        
        # Query loop for selected topic
        while True:
            # Get user's question
            query = ui.get_user_query(topic)
            
            ui.display_loading()
            
            # Generate answer
            response, is_fallback = chatbot.generate_answer(
                query, topic, difficulty
            )
            
            # Display response
            ui.display_response(response, is_fallback)
            
            # Ask if user wants to continue with this topic
            if not ui.ask_continue():
                break
        
        # Ask if user wants to select another topic
        print("\n" + "─" * 54)
        another = input(">>> অন্য বিষয় নির্বাচন করতে চান? (Select another topic?) (হ্যাঁ/না): ").strip().lower()
        
        if another not in ['হ্যাঁ', 'yes', 'y', 'জি', 'হ']:
            ui.display_goodbye()
            break
        
        print()


if __name__ == '__main__':
    main()

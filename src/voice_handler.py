"""Voice handler for STT (Speech-to-Text) and TTS (Text-to-Speech) support"""

try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False


class VoiceHandler:
    """
    Handle speech-to-text and text-to-speech for Bangla
    
    Note: This is a bonus feature. Install dependencies with:
    pip install pyttsx3 gtts SpeechRecognition
    """
    
    def __init__(self, language: str = 'bn'):
        """
        Initialize voice handler
        
        Args:
            language: Language code ('bn' for Bengali, 'en' for English)
        """
        self.language = language
        self.tts_engine = self._init_tts()
        self.recognizer = self._init_recognizer()

    def _init_tts(self):
        """Initialize TTS engine"""
        if not PYTTSX3_AVAILABLE:
            print("⚠️  Warning: pyttsx3 not installed. TTS not available.")
            return None
        
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Speed
            return engine
        except Exception as e:
            print(f"⚠️  Error initializing TTS: {e}")
            return None

    def _init_recognizer(self):
        """Initialize speech recognizer"""
        if not SR_AVAILABLE:
            print("⚠️  Warning: SpeechRecognition not installed. STT not available.")
            return None
        
        try:
            return sr.Recognizer()
        except Exception as e:
            print(f"⚠️  Error initializing STT: {e}")
            return None

    def speak(self, text: str, use_gtts: bool = False) -> bool:
        """
        Convert text to speech
        
        Args:
            text: Text to speak (Bengali or English)
            use_gtts: Use Google TTS instead of pyttsx3
            
        Returns:
            True if successful, False otherwise
        """
        if use_gtts:
            return self._speak_gtts(text)
        else:
            return self._speak_pyttsx3(text)

    def _speak_pyttsx3(self, text: str) -> bool:
        """Speak using pyttsx3"""
        if not self.tts_engine or not PYTTSX3_AVAILABLE:
            print("❌ pyttsx3 not available")
            return False
        
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            return True
        except Exception as e:
            print(f"❌ Error speaking: {e}")
            return False

    def _speak_gtts(self, text: str) -> bool:
        """Speak using Google Text-to-Speech"""
        if not GTTS_AVAILABLE:
            print("❌ gTTS not available")
            return False
        
        try:
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save("/tmp/response.mp3")
            
            # Try to play with system command
            import os
            os.system("afplay /tmp/response.mp3")  # macOS
            # On Linux: os.system("mpg123 /tmp/response.mp3")
            # On Windows: os.system("start /tmp/response.mp3")
            
            return True
        except Exception as e:
            print(f"❌ Error with gTTS: {e}")
            return False

    def recognize(self) -> str:
        """
        Recognize speech from microphone
        
        Returns:
            Recognized text or empty string if failed
        """
        if not self.recognizer or not SR_AVAILABLE:
            print("❌ Speech Recognition not available")
            return ""
        
        try:
            with sr.Microphone() as source:
                print("🎤 শুনছি... (Listening...)")
                audio = self.recognizer.listen(source, timeout=10)
            
            # Try to recognize Bengali speech
            try:
                text = self.recognizer.recognize_google(audio, language='bn-IN')
                print(f"✅ চিনেছি: {text}")
                return text
            except sr.UnknownValueError:
                print("❌ বুঝতে পারলাম না। (Could not understand)")
                return ""
            except sr.RequestError as e:
                print(f"❌ API Error: {e}")
                return ""
                
        except Exception as e:
            print(f"❌ Error recording: {e}")
            return ""

    def interactive_mode(self):
        """Run interactive voice chat mode"""
        print("""
╔════════════════════════════════════════════════════════╗
║          ভয়েস মোড (Voice Mode) - বোনাস            ║
╚════════════════════════════════════════════════════════╝
        """)
        
        while True:
            try:
                # Get voice input
                user_input = self.recognize()
                if not user_input:
                    continue
                
                # This would integrate with the chatbot
                print(f"\nআপনার প্রশ্ন: {user_input}\n")
                
                # Simulate response
                response = f"আপনার প্রশ্ন প্রক্রিয়া করছি: {user_input}"
                
                # Speak response
                self.speak(response, use_gtts=True)
                
                # Ask to continue
                continue_response = input("\nআরও কিছু বলতে চান? (আছে/নেই): ").strip()
                if continue_response.lower() in ['নেই', 'no', 'n']:
                    break
                    
            except KeyboardInterrupt:
                print("\n\nবন্ধ করা হচ্ছে... (Exiting)")
                break
            except Exception as e:
                print(f"Error: {e}")
                break

    @staticmethod
    def check_dependencies() -> dict:
        """
        Check which voice dependencies are installed
        
        Returns:
            Dictionary with availability status
        """
        return {
            'pyttsx3': PYTTSX3_AVAILABLE,
            'gtts': GTTS_AVAILABLE,
            'speech_recognition': SR_AVAILABLE,
            'all_available': all([PYTTSX3_AVAILABLE, GTTS_AVAILABLE, SR_AVAILABLE])
        }


def setup_voice_support():
    """Setup instructions for voice support"""
    print("""
╔════════════════════════════════════════════════════════╗
║        ভয়েস সাপোর্ট সেটআপ (Voice Support Setup)   ║
╚════════════════════════════════════════════════════════╝

ভয়েস ফিচার সক্রিয় করতে নিম্নলিখিত প্যাকেজ ইনস্টল করুন:

pip install pyttsx3 gtts SpeechRecognition

ম্যাক-এ microphone অ্যাক্সেস দেওয়ার জন্য:
System Preferences > Security & Privacy > Microphone > Allow

ব্যবহার:
from src.voice_handler import VoiceHandler

voice = VoiceHandler(language='bn')

# Text to Speech
voice.speak("আমাদের চ্যাটবটে স্বাগতম")

# Speech to Text (requires microphone)
text = voice.recognize()

# Interactive mode
voice.interactive_mode()
""")


if __name__ == '__main__':
    # Check dependencies
    deps = VoiceHandler.check_dependencies()
    print(f"Dependencies available: {deps}")
    
    # If all dependencies available, run interactive mode
    if deps['all_available']:
        voice = VoiceHandler(language='bn')
        voice.interactive_mode()
    else:
        setup_voice_support()

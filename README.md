# 🇧🇩 Bangla FAQ Chatbot - RAG System

A comprehensive Retrieval-Augmented Generation (RAG) based FAQ chatbot for Bengali language with support for 5 major topics, metadata filtering, and fallback mechanisms.

## 📋 Features

### Core Features
- ✅ **5 Bangla Topics**: শিক্ষা, স্বাস্থ্য, ভ্রমণ, প্রযুক্তি, খেলাধুলা
- ✅ **Menu/Routing System**: Interactive topic selection and navigation
- ✅ **Metadata Filtering**: Filter FAQs by topic and difficulty level
- ✅ **RAG Implementation**: Semantic search with similarity matching
- ✅ **Bangla I/O Support**: Full Unicode Bengali input/output support
- ✅ **15+ FAQs**: 3+ FAQs per topic with comprehensive metadata
- ✅ **Fallback Responses**: Smart fallback for non-matching queries
- ✅ **Simple Interface**: Console-based interactive UI

### Bonus Features
- 🎤 **Voice Support (STT/TTS)**: Optional voice input/output (requires additional setup)
- 🧪 **Unit Tests**: Comprehensive test suite for all components
- 📊 **Statistics**: FAQ database statistics and analytics

## 🚀 Quick Start

### Installation

1. **Clone/Download the project**
```bash
cd /Users/rizon/Desktop/ML/Assignment-17
```

2. **Create virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Chatbot

**Interactive Console Mode:**
```bash
python3 main.py
```

**Run Demo Script:**
```bash
python3 demo_script.py
```

**Run Tests:**
```bash
python3 -m pytest tests/ -v
# OR
python3 -m unittest tests/test_components.py -v
```

## 📁 Project Structure

```
Assignment-17/
├── context.md                    # Project documentation
├── requirements.txt              # Python dependencies
├── main.py                       # Main interactive chatbot
├── demo_script.py               # Demo and testing script
├── console_ui.py                # Console UI and menus
├── README.md                    # This file
├── data/
│   └── bangla_faqs.json        # FAQ database (15+ FAQs)
├── src/
│   ├── __init__.py
│   ├── bangla_processor.py      # Bangla text normalization & processing
│   ├── metadata_filter.py       # Topic/difficulty filtering
│   ├── faq_retriever.py         # RAG retrieval (semantic search)
│   ├── response_generator.py    # Response generation & fallback
│   └── chatbot.py               # Main chatbot orchestration
└── tests/
    └── test_components.py       # Unit tests
```

## 📊 FAQ Database Structure

Each FAQ entry contains:
```json
{
  "id": "unique_identifier",
  "topic": "শিক্ষা",
  "difficulty": "সহজ|মাঝারি|কঠিন",
  "question": "প্রশ্ন বাংলায়",
  "answer": "উত্তর বাংলায়",
  "keywords": ["কীওয়ার্ড1", "কীওয়ার্ড2"],
  "tags": ["ট্যাগ1", "ট্যাগ2"]
}
```

**Topics:**
1. **শিক্ষা** (Education) - 3 FAQs
2. **স্বাস্থ্য** (Health) - 3 FAQs
3. **ভ্রমণ** (Travel) - 3 FAQs
4. **প্রযুক্তি** (Technology) - 3 FAQs
5. **খেলাধুলা** (Sports) - 3 FAQs

**Difficulty Levels:**
- সহজ (Easy)
- মাঝারি (Medium)
- কঠিন (Hard)

## 🤖 How It Works

### RAG Pipeline
1. **User Input**: User selects topic and asks a question
2. **Text Processing**: Normalize Bangla text and tokenize
3. **Filtering**: Filter FAQs by selected topic and difficulty
4. **Retrieval**: Use semantic search to find relevant FAQs
5. **Ranking**: Rank results by similarity score
6. **Generation**: Generate response from best match or fallback

### Similarity Matching
- **Algorithm**: Jaccard similarity with keyword boost
- **Tokenization**: Word-level tokenization for Bengali text
- **Stop Words**: Removal of common Bengali stop words
- **Confidence Threshold**: 0.1 (configurable)

## 🎯 Usage Examples

### Interactive Mode
```bash
$ python3 main.py

╔════════════════════════════════════════════════════════╗
║           বাংলা FAQ চ্যাটবট স্বাগতম             ║
╚════════════════════════════════════════════════════════╝

বিষয় নির্বাচন করুন:
1. 📚 শিক্ষা
2. 🏥 স্বাস্থ্য
3. ✈️  ভ্রমণ
4. 💻 প্রযুক্তি
5. ⚽ খেলাধুলা
0. 🚪 বের হন

>>> আপনার পছন্দ: 1

>>> আপনার প্রশ্ন: পড়াশোনায় মনোযোগ বাড়ানোর উপায় কি?

✅ প্রাসঙ্গিক উত্তর পাওয়া গেছে:

উত্তর:
মনোযোগ বাড়াতে নিয়মিত সময়সূচী অনুসরণ করুন, স্মার্টফোন এবং অন্যান্য ডিভাইস দূরে রাখুন...

[প্রাসঙ্গিকতা স্তর: কঠিন | আত্মবিশ্বাস: 75%]
```

### Programmatic Usage
```python
from src.chatbot import BanglaFAQChatbot

chatbot = BanglaFAQChatbot('data/bangla_faqs.json')

# Get answer for a question
response, is_fallback = chatbot.generate_answer(
    "পড়াশোনায় মনোযোগ বাড়ানোর উপায়?",
    topic="শিক্ষা",
    difficulty="কঠিন"
)

print(response)
```

## 🧪 Testing

Run the unit tests:
```bash
python3 -m unittest tests/test_components.py -v
```

Key test cases:
- Bengali text normalization
- Topic and difficulty validation
- FAQ filtering and retrieval
- Response generation
- Fallback handling

## 📹 Demo

Run the demo script to see all features in action:
```bash
python3 demo_script.py
```

**Demo Features:**
- ✅ Basic Q&A for all 5 topics
- ✅ Fallback responses for non-existent answers
- ✅ Difficulty-based filtering
- ✅ Chatbot statistics

## 🎤 Bonus: Voice Support (Optional)

### STT/TTS Implementation
To enable voice support, install additional packages:
```bash
pip install google-cloud-speech gtts pyttsx3
```

### Usage
```python
from src.voice_handler import VoiceHandler

voice = VoiceHandler()

# Convert speech to text
text = voice.recognize_speech()

# Convert text to speech
voice.speak(text)
```

## 📝 Code Components

### `bangla_processor.py`
- Text normalization (diacritic removal)
- Tokenization
- Stop word removal
- Keyword extraction
- Similarity calculation

### `metadata_filter.py`
- Topic validation and filtering
- Difficulty level filtering
- Combined filtering support
- Valid topic/difficulty getters

### `faq_retriever.py`
- FAQ database loading (JSON)
- Semantic search implementation
- Similarity ranking
- Result retrieval (top-k)

### `response_generator.py`
- Response formatting
- Fallback message selection
- Metadata inclusion
- Context-aware responses

### `chatbot.py`
- RAG pipeline orchestration
- Question answering
- Statistics generation
- Multi-result search

### `console_ui.py`
- Menu display and navigation
- User input handling
- Response formatting
- Interactive flow

## ⚙️ Configuration

### Adjustable Parameters

**In `src/chatbot.py`:**
```python
CONFIDENCE_THRESHOLD = 0.1  # Minimum similarity score
```

**In `faq_retriever.py`:**
```python
top_k = 1  # Number of results to return
```

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'sentence_transformers'`
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: `FileNotFoundError: FAQ file not found`
**Solution:** Ensure you're running from the project root directory:
```bash
cd /Users/rizon/Desktop/ML/Assignment-17
```

### Issue: Bengali text shows as garbled
**Solution:** Ensure your terminal supports UTF-8:
```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

## 📚 Technologies Used

- **Python 3.8+**
- **sentence-transformers**: For semantic embeddings (optional)
- **NLTK/spaCy**: For text processing
- **JSON**: For FAQ database
- **unittest**: For testing
- **google-cloud-speech** (bonus): For STT
- **gTTS/pyttsx3** (bonus): For TTS

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ RAG (Retrieval-Augmented Generation) pipeline
- ✅ Semantic search and similarity matching
- ✅ Metadata filtering and indexing
- ✅ Bengali NLP and Unicode handling
- ✅ Chatbot design and conversation flow
- ✅ Python OOP and design patterns
- ✅ Interactive CLI development
- ✅ Unit testing and quality assurance

## 📄 License

Educational project - Free to use and modify

## 👨‍💻 Author

Student | ML Assignment 17

## 🔗 References

- [Bengali NLP Resources](https://github.com/csebuetnlp/BanglaNLP)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS Documentation](https://faiss.ai/)
- [RAG Tutorials](https://huggingface.co/course/chapter7)

---

**Version:** 1.0.0  
**Last Updated:** January 22, 2026  
**Status:** Production Ready ✅

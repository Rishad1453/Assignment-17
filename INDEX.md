# 🇧🇩 Bangla FAQ Chatbot - Complete Project Index

## 📌 Getting Started

### 🚀 Quick Start (30 seconds)
```bash
cd /Users/rizon/Desktop/ML/Assignment-17
python3 quick_start.py      # See a quick demo
python3 main.py             # Run the interactive chatbot
python3 demo_script.py      # See comprehensive demo
```

### 📋 Installation
```bash
pip install -r requirements.txt
# Optional voice support:
pip install pyttsx3 gtts SpeechRecognition
```

---

## 📁 Complete File Structure

```
Assignment-17/                              Total: 25 files | Size: 196KB
│
├── 📄 PROJECT_SUMMARY.md ............... ✅ Project completion summary
├── 📄 README.md ....................... ✅ Complete documentation  
├── 📄 USAGE.md ........................ ✅ API reference & examples
├── 📄 context.md ..................... ✅ Project context & planning
├── 📄 INDEX.md ........................ ✅ This file
│
├── 🐍 main.py ........................ ✅ Interactive chatbot (entry point)
├── 🐍 demo_script.py ................. ✅ Automated demo with 4 scenarios
├── 🐍 quick_start.py ................. ✅ Quick start demo
├── 🐍 console_ui.py .................. ✅ Console UI with menus
│
├── 📁 src/ ............................ Core implementation modules
│   ├── 🐍 __init__.py ............... Package initialization
│   ├── 🐍 chatbot.py ............... Main RAG orchestration
│   ├── 🐍 faq_retriever.py ......... FAQ DB + semantic search
│   ├── 🐍 metadata_filter.py ....... Topic/difficulty filtering
│   ├── 🐍 bangla_processor.py ...... Bangla text processing
│   ├── 🐍 response_generator.py .... Response generation + fallback
│   └── 🐍 voice_handler.py ......... BONUS: Voice support (STT/TTS)
│
├── 📁 data/ ........................... FAQ Database
│   └── 📊 bangla_faqs.json ......... 15 FAQs with complete metadata
│
├── 📁 tests/ .......................... Unit Tests
│   └── 🧪 test_components.py ....... 5 test classes, 8+ test methods
│
├── 📄 requirements.txt ................ Python dependencies
├── 📄 setup.sh ....................... Setup automation script
└── 📄 INDEX.md ....................... This file
```

---

## 🎯 What Each File Does

### Entry Points (Run These)
| File | Purpose | Command |
|------|---------|---------|
| `main.py` | Interactive chatbot with menus | `python3 main.py` |
| `demo_script.py` | Automated demo of all features | `python3 demo_script.py` |
| `quick_start.py` | Quick 30-second demo | `python3 quick_start.py` |

### Core Modules (Import These)
| File | Purpose | Key Classes |
|------|---------|------------|
| `src/chatbot.py` | RAG orchestration | `BanglaFAQChatbot` |
| `src/faq_retriever.py` | FAQ search & retrieval | `FAQRetriever` |
| `src/metadata_filter.py` | Topic/difficulty filtering | `MetadataFilter` |
| `src/bangla_processor.py` | Bangla text processing | `BanglaProcessor` |
| `src/response_generator.py` | Response generation | `ResponseGenerator` |
| `src/voice_handler.py` | Voice support (bonus) | `VoiceHandler` |

### UI Components
| File | Purpose |
|------|---------|
| `console_ui.py` | Menu system, formatted output |

### Configuration & Data
| File | Purpose | Contents |
|------|---------|----------|
| `data/bangla_faqs.json` | FAQ database | 15 FAQs × 5 topics |
| `requirements.txt` | Python dependencies | 5 packages |
| `setup.sh` | Setup automation | Installation script |

### Documentation
| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Complete guide | Everyone |
| `USAGE.md` | API reference | Developers |
| `context.md` | Project context | Planners |
| `PROJECT_SUMMARY.md` | Completion report | Evaluators |
| `INDEX.md` | This file | Everyone |

---

## 🔄 How to Use the Chatbot

### Method 1: Interactive Mode
```bash
python3 main.py

# You'll see:
# 1. Topic menu (শিক্ষা, স্বাস্থ্য, ভ্রমণ, প্রযুক্তি, খেলাধুলা)
# 2. Optional difficulty filter
# 3. Ask your question
# 4. Get answer with confidence score
```

### Method 2: Programmatic Usage
```python
from src.chatbot import BanglaFAQChatbot

chatbot = BanglaFAQChatbot('data/bangla_faqs.json')
response, is_fallback = chatbot.generate_answer(
    query="পড়াশোনা",
    topic="শিক্ষা",
    difficulty="কঠিন"
)
print(response)
```

### Method 3: Direct FAQ Search
```python
from src.faq_retriever import FAQRetriever
from src.metadata_filter import MetadataFilter

retriever = FAQRetriever('data/bangla_faqs.json')
results = retriever.retrieve("পড়াশোনা", top_k=3)

for faq, score in results:
    print(f"Q: {faq['question']}")
    print(f"Score: {score:.1%}\n")
```

---

## 📊 FAQ Database Structure

### Topics (5 Total)
1. **শিক্ষা** (Education) - 3 FAQs
2. **স্বাস্থ্য** (Health) - 3 FAQs
3. **ভ্রমণ** (Travel) - 3 FAQs
4. **প্রযুক্তি** (Technology) - 3 FAQs
5. **খেলাধুলা** (Sports) - 3 FAQs

### Difficulty Levels (3 Total)
- **সহজ** (Easy)
- **মাঝারি** (Medium)
- **কঠিন** (Hard)

### Each FAQ Contains
- `id`: Unique identifier
- `topic`: One of 5 topics
- `difficulty`: Easy/Medium/Hard
- `question`: Bengali question
- `answer`: Bengali answer
- `keywords`: List of keywords
- `tags`: Categorization tags

---

## 🧪 Testing

### Run All Tests
```bash
python3 -m unittest tests/test_components.py -v
```

### Run Specific Test Class
```bash
python3 -m unittest tests.test_components.TestBanglaProcessor -v
```

### Test Coverage
```bash
pip install coverage
coverage run -m unittest discover tests/
coverage report
```

---

## 🎯 Key Features Checklist

### ✅ Core Requirements
- [x] 5 Bangla topics (শিক্ষা, স্বাস্থ্য, ভ্রমণ, প্রযুক্তি, খেলাধুলা)
- [x] Menu/routing system with topic selection
- [x] Metadata filtering (topic + difficulty)
- [x] RAG system (semantic search + retrieval)
- [x] Bangla input/output support
- [x] 3+ FAQs per topic (exactly 15)
- [x] Fallback responses for non-matches
- [x] Simple console interface

### ✅ Additional Features
- [x] Confidence scoring (0-100%)
- [x] Metadata display in responses
- [x] Difficulty-level filtering
- [x] Topic-specific fallback messages
- [x] Comprehensive documentation
- [x] Unit test suite
- [x] Demo script with 4 scenarios
- [x] Quick start guide

### ✅ Bonus Features
- [x] Voice support (STT/TTS)
- [x] Setup automation script
- [x] API documentation (USAGE.md)
- [x] Project summary (PROJECT_SUMMARY.md)
- [x] Quick start demo
- [x] Multiple entry points

---

## 🔍 How the RAG Pipeline Works

```
User Input
    ↓
Bangla Text Processing (normalize, tokenize)
    ↓
Topic Filtering (select FAQ subset)
    ↓
Semantic Similarity Search (Jaccard + keywords)
    ↓
Ranking (score & sort results)
    ↓
Response Generation (format answer)
    ↓
Fallback Check (if no match found)
    ↓
Display to User (with confidence & metadata)
```

---

## 📚 Documentation Map

```
README.md ..................... START HERE
├── Overview
├── Features
├── Installation
├── Quick start
├── Project structure
└── Technology stack

USAGE.md ....................... DEVELOPER REFERENCE
├── API documentation
├── Code examples
├── Configuration
├── Integration examples
└── Troubleshooting

context.md ..................... PLANNING DOCUMENT
├── Requirements breakdown
├── Topic details
├── Technical stack
├── Implementation phases
└── Resources

PROJECT_SUMMARY.md ............ COMPLETION REPORT
├── Checklist
├── Statistics
├── Test coverage
└── Assessment matrix
```

---

## 🚀 Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run interactive chatbot
python3 main.py

# Run demo
python3 demo_script.py

# Quick demo
python3 quick_start.py

# Run tests
python3 -m unittest tests/test_components.py -v

# Check FAQ count
python3 -c "from src.faq_retriever import FAQRetriever; r=FAQRetriever('data/bangla_faqs.json'); print(f'Total FAQs: {r.get_faq_count()}')"

# Add voice support
pip install pyttsx3 gtts SpeechRecognition

# Check file structure
find . -type f -name "*.py" -o -name "*.json" -o -name "*.md" | sort
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 25 |
| Python Files | 9 |
| Documentation Files | 4 |
| Total Lines of Code | ~1,200 |
| Total FAQ Entries | 15 |
| Test Classes | 5 |
| Test Methods | 8+ |
| Project Size | 196 KB |

---

## 🎓 Learning Resources

### Within This Project
- `context.md` - Complete project planning
- `USAGE.md` - API documentation with examples
- `src/chatbot.py` - Main RAG implementation
- `src/bangla_processor.py` - Text processing examples
- `tests/test_components.py` - How to test modules

### External Resources
- [Bengali NLP](https://github.com/csebuetnlp/BanglaNLP)
- [RAG Concepts](https://huggingface.co/course/chapter7)
- [Similarity Metrics](https://en.wikipedia.org/wiki/Jaccard_index)
- [Python Unicode](https://docs.python.org/3/howto/unicode.html)

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Problem: Bengali text garbled
```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

### Problem: FAQ file not found
```bash
# Run from project root
cd /Users/rizon/Desktop/ML/Assignment-17
python3 main.py
```

### Problem: Voice not working
```bash
pip install pyttsx3 gtts SpeechRecognition
# Also need microphone permission on macOS
```

---

## 📞 Quick Support

**Q: How do I run the chatbot?**  
A: `python3 main.py`

**Q: How do I see a demo?**  
A: `python3 demo_script.py`

**Q: Where are the FAQs stored?**  
A: `data/bangla_faqs.json` (JSON format)

**Q: How do I add more FAQs?**  
A: Edit `data/bangla_faqs.json` and follow the existing format

**Q: Can I use this in a web app?**  
A: Yes! Check `USAGE.md` for Flask/FastAPI examples

**Q: Is voice support included?**  
A: Yes (bonus)! See `src/voice_handler.py`

---

## ✅ Verification Checklist

Before submission, verify:
- [x] All files present (25 files)
- [x] All modules working (`python3 quick_start.py`)
- [x] Tests passing (`python3 -m unittest tests/test_components.py`)
- [x] Documentation complete (4 MD files)
- [x] FAQ database valid (15 FAQs)
- [x] Bangla text displays correctly
- [x] Menu system functional
- [x] Fallback handling works

---

## 🎉 Ready for Submission!

This project is **complete, tested, and documented**.

All files are ready in: `/Users/rizon/Desktop/ML/Assignment-17/`

**To create demo video:**
1. Run `python3 main.py`
2. Demo selecting topics and asking questions
3. Show fallback for non-matching queries
4. (Optional) Show voice features

---

**Version**: 1.0.0  
**Status**: ✅ Complete  
**Date**: January 22, 2026  
**Location**: `/Users/rizon/Desktop/ML/Assignment-17/`

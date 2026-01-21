# Bangla FAQ Chatbot with RAG - Project Context

## Project Overview
Build a **Retrieval-Augmented Generation (RAG)** based FAQ chatbot that supports **5 Bangla topics** with metadata filtering, menu routing, and multi-modal support (text + optional voice).

---

## 📋 Project Requirements

### Core Features (Must Have)
1. **5 Bangla Topics** - শিক্ষা, স্বাস্থ্য, ভ্রমণ, প্রযুক্তি, খেলাধুলা
2. **Menu/Routing System** - User selects a category before querying
3. **Metadata Filtering** - Filter FAQs by topic & difficulty level
4. **RAG Implementation** - Retrieve relevant FAQs + generate answers
5. **Bangla I/O Support** - Full Unicode Bangla input/output
6. **3+ FAQs per Topic** - Minimum 15 FAQs total
7. **Fallback Response** - Custom message when no matching FAQ found
8. **Simple Interface** - Console or web-based UI

### Bonus Features (Optional)
- **STT/TTS Support** - Voice input/output for Bangla

---

## 🏗️ Project Structure

```
/Users/rizon/Desktop/ML/Assignment-17/
├── README.md                    # Project documentation
├── context.md                   # This file
├── requirements.txt             # Python dependencies
├── faq_database.json           # FAQ dataset with metadata
├── src/
│   ├── __init__.py
│   ├── faq_retriever.py        # RAG retrieval logic
│   ├── metadata_filter.py      # Filtering by topic/difficulty
│   ├── bangla_processor.py     # Bangla text processing
│   ├── response_generator.py   # Generate final responses
│   ├── voice_handler.py        # STT/TTS (bonus)
│   └── chatbot.py              # Main chatbot logic
├── data/
│   └── bangla_faqs.json        # FAQ dataset file
├── console_ui.py               # Console interface
├── web_ui.py                   # Web interface (optional)
├── demo_script.py              # Demo/testing script
└── tests/
    └── test_*.py               # Unit tests
```

---

## 📊 FAQ Dataset Structure

### Format: `faq_database.json`
Each FAQ should have:
```json
{
  "id": "unique_id",
  "topic": "শিক্ষা",
  "difficulty": "সহজ|মাঝারি|কঠিন",
  "question": "প্রশ্ন বাংলায়",
  "answer": "উত্তর বাংলায়",
  "keywords": ["কীওয়ার্ড1", "কীওয়ার্ড2"],
  "tags": ["ট্যাগ1", "ট্যাগ2"]
}
```

### Topics & Difficulty Levels
- **Topics**: শিক্ষা, স্বাস্থ্য, ভ্রমণ, প্রযুক্তি, খেলাধুলা
- **Difficulty**: সহজ (Easy), মাঝারি (Medium), কঠিন (Hard)

---

## 5️⃣ Topic Breakdown: Sample FAQs

### 1. **শিক্ষা (Education)**
- Q: বিশ্ববিদ্যালয়ে ভর্তির জন্য কী কী যোগ্যতা লাগে?
- Q: অনলাইন শিক্ষা কি কার্যকর?
- Q: পড়াশোনায় মনোযোগ বাড়ানোর উপায় কি?

### 2. **স্বাস্থ্য (Health)**
- Q: ডায়াবেটিস রোগীদের জন্য সঠিক খাবার কি?
- Q: মাইগ্রেনের ব্যথা কমানোর উপায় কি?
- Q: প্রতিদিন কতটা পানি পান করা উচিত?

### 3. **ভ্রমণ (Travel)**
- Q: বাংলাদেশে সবচেয়ে ভালো পর্যটন স্থান কোথায়?
- Q: দেশের বাইরে ভ্রমণের জন্য পাসপোর্ট কিভাবে পাই?
- Q: বাজেটে ঘুরে আসা সম্ভব কি?

### 4. **প্রযুক্তি (Technology)**
- Q: কৃত্রিম বুদ্ধিমত্তা কি এবং এর প্রয়োগ কোথায়?
- Q: ক্লাউড স্টোরেজ নিরাপদ কি?
- Q: নতুন প্রযুক্তি শিখতে কোন কোর্স নিব?

### 5. **খেলাধুলা (Sports)**
- Q: ক্রিকেটে একজন ভালো ব্যাটসম্যান হতে কি লাগে?
- Q: ফুটবলে একটি দলে কতজন খেলোয়াড় থাকে?
- Q: যোগব্যায়াম কেন উপকারী?

---

## 🔧 Technical Stack

### Backend
- **Language**: Python 3.8+
- **RAG Framework**: Sentence Transformers + FAISS (or simple TF-IDF)
- **NLP Libraries**: 
  - `sentence-transformers` - For semantic search
  - `nltk` / `spaCy` - Bangla text processing
  - `transformers` - For embeddings
- **Web Framework**: Flask/FastAPI (optional)

### Frontend
- **Console UI**: Python `cmd` module or simple `input()`
- **Web UI** (optional): HTML + JavaScript + Flask/FastAPI

### Voice (Bonus)
- **STT**: `google-cloud-speech` or `pyttsx3`
- **TTS**: `gTTS` (Google Text-to-Speech) or `pyttsx3`

### Dependencies File: `requirements.txt`
```
sentence-transformers==2.2.2
faiss-cpu==1.7.4
numpy==1.24.0
python-dotenv==1.0.0
flask==2.3.0
nltk==3.8.1
gTTS==2.3.1
google-cloud-speech==2.20.0
pyttsx3==2.90
```

---

## 🛠️ Implementation Steps

### Phase 1: Data Preparation
1. Create `faq_database.json` with 5 topics × 3+ FAQs each
2. Add metadata: topic, difficulty, keywords, tags
3. Ensure all text is in Bangla (UTF-8 encoding)

### Phase 2: Core RAG System
1. **FAQ Retriever** (`faq_retriever.py`)
   - Load FAQ dataset from JSON
   - Implement semantic search using embeddings
   - Alternative: TF-IDF for simpler approach
   
2. **Metadata Filter** (`metadata_filter.py`)
   - Filter by topic (required)
   - Filter by difficulty level (optional)
   - Return filtered FAQs to retriever

3. **Bangla Processor** (`bangla_processor.py`)
   - Normalize Bangla text (handle دiacritics)
   - Tokenization
   - Keyword extraction

4. **Response Generator** (`response_generator.py`)
   - Rank retrieved FAQs by relevance
   - Generate response from top match
   - Add fallback message if no match found

### Phase 3: Menu & Routing
1. Build menu system (`console_ui.py`)
   ```
   ========== বাংলা FAQ চ্যাটবট ==========
   1. শিক্ষা (Education)
   2. স্বাস্থ্য (Health)
   3. ভ্রমণ (Travel)
   4. প্রযুক্তি (Technology)
   5. খেলাধুলা (Sports)
   0. বের হন (Exit)
   
   আপনার পছন্দ: 
   ```

2. Route user input to correct topic filter
3. Display Q&A with difficulty level

### Phase 4: Integration
1. Main chatbot engine (`chatbot.py`)
   - Orchestrate retriever, filter, generator
   - Handle user session

2. Testing & debugging
3. Create demo script (`demo_script.py`)

### Phase 5: Bonus - Voice Support (Optional)
1. **STT Module** (`voice_handler.py`)
   - Capture Bangla speech input
   - Convert to text
   
2. **TTS Module**
   - Convert response text to Bangla speech
   - Play audio

---

## 📝 Code Architecture & Key Functions

### `faq_retriever.py`
```python
class FAQRetriever:
    def __init__(self, faq_file_path):
        # Load FAQ dataset
        
    def load_faqs(self):
        # Load from JSON
        
    def retrieve(self, query, topic_filter=None, difficulty=None):
        # Semantic search + metadata filtering
        # Return top-k matches with scores
        
    def get_embeddings(self, text):
        # Get semantic embeddings for query
```

### `metadata_filter.py`
```python
class MetadataFilter:
    def filter_by_topic(self, faqs, topic):
        # Filter FAQs by selected topic
        
    def filter_by_difficulty(self, faqs, difficulty):
        # Optional: filter by difficulty level
        
    def apply_filters(self, faqs, topic, difficulty=None):
        # Apply combined filters
```

### `console_ui.py`
```python
def display_menu():
    # Show topic selection menu
    
def get_user_topic():
    # Get user's topic choice
    
def get_user_query(topic):
    # Get user's question for selected topic
    
def display_response(answer, difficulty, source_question):
    # Display retrieved answer with metadata
```

### `chatbot.py` (Main Logic)
```python
class BanglaFAQChatbot:
    def __init__(self, faq_database_path):
        self.retriever = FAQRetriever(faq_database_path)
        self.filter = MetadataFilter()
        
    def answer_question(self, query, topic, difficulty=None):
        # 1. Filter FAQs by topic
        filtered_faqs = self.filter.apply_filters(
            self.retriever.faqs, topic, difficulty
        )
        
        # 2. Retrieve relevant FAQs
        results = self.retriever.retrieve(
            query, 
            filtered_faqs
        )
        
        # 3. Generate response
        if results:
            return self.generate_response(results[0])
        else:
            return self.get_fallback_response(topic)
            
    def generate_response(self, faq_match):
        # Format and return answer
        
    def get_fallback_response(self, topic):
        # Return: "দুঃখিত, এই প্রশ্নের উত্তর আমার কাছে নেই।"
```

---

## 🎯 RAG Implementation Details

### Approach 1: Semantic Search (Recommended)
```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# Encode FAQ questions
faq_embeddings = model.encode(faq_questions)

# Encode user query
query_embedding = model.encode(user_query)

# Find most similar FAQs
hits = util.semantic_search(query_embedding, faq_embeddings, top_k=3)
```

### Approach 2: TF-IDF (Simpler Alternative)
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(faq_questions)
query_vector = vectorizer.transform([user_query])
similarity = cosine_similarity(query_vector, tfidf_matrix)
```

---

## 💬 Example Interaction Flow

```
========== বাংলা FAQ চ্যাটবট ==========
বিষয় নির্বাচন করুন:
1. শিক্ষা
2. স্বাস্থ্য
3. ভ্রমণ
4. প্রযুক্তি
5. খেলাধুলা
0. বের হন

>> আপনার পছন্দ: 1

>> আপনার প্রশ্ন (শিক্ষা): পড়াশোনায় মনোযোগ বাড়ানোর উপায় কি?

[চ্যাটবট বিশ্লেষণ করছে...]

প্রাসঙ্গিক উত্তর:
Q: পড়াশোনায় মনোযোগ বাড়ানোর উপায় কি?
A: মনোযোগ বাড়াতে নিয়মিত পড়ুন, ডিভাইস দূরে রাখুন, এবং ছোট ব্রেক নিন।
[কঠিন স্তর]

আরও প্রশ্ন? (হ্যাঁ/না): না

ধন্যবাদ! পুনরায় দেখা হবে।
```

---

## ✅ Testing & Validation

### Test Cases
1. **Valid Query** - User asks question related to FAQ
   - Expected: Top matching FAQ returned
   
2. **Ambiguous Query** - Multiple FAQs match
   - Expected: Best match returned with confidence score
   
3. **No Match** - User asks unrelated question
   - Expected: Fallback response displayed
   
4. **Wrong Topic** - User selects topic but asks about different topic
   - Expected: Still filtered by selected topic, fallback if no match
   
5. **Bangla Input Handling** - Unicode Bangla characters
   - Expected: Proper text processing, no encoding errors

### Demo Script (`demo_script.py`)
```python
def run_demo():
    chatbot = BanglaFAQChatbot('faq_database.json')
    
    test_cases = [
        ("শিক্ষা", "পড়াশোনায় মনোযোগ বাড়ানোর উপায়?"),
        ("স্বাস্থ্য", "ডায়াবেটিস কি?"),
        ("ভ্রমণ", "সিলেট যেতে হলে কিভাবে যাব?"),
        ("প্রযুক্তি", "AI কি?"),
        ("খেলাধুলা", "ক্রিকেটের নিয়ম কি?"),
    ]
    
    for topic, query in test_cases:
        response = chatbot.answer_question(query, topic)
        print(f"Topic: {topic}")
        print(f"Query: {query}")
        print(f"Response: {response}\n")
```

---

## 📹 Demo Video Requirements

Record a **2-3 minute video** showing:
1. **Menu Selection** - User navigates to a topic
2. **Valid Query** - Ask a question, get matching FAQ answer
3. **Fallback Response** - Ask unrelated question, show fallback message
4. **Multiple Topics** - Demonstrate 2-3 different topics
5. **Bangla Text** - Clearly show Bangla input/output working correctly
6. **(Optional)** Voice demo if STT/TTS implemented

**Video Format**: MP4, .mov, or .webm
**Audio**: Clear narration in Bangla or English

---

## 🚀 Submission Checklist

- [ ] `faq_database.json` - 5 topics × 3+ FAQs with metadata
- [ ] `src/faq_retriever.py` - RAG retrieval logic
- [ ] `src/metadata_filter.py` - Topic/difficulty filtering
- [ ] `src/bangla_processor.py` - Bangla text processing
- [ ] `src/response_generator.py` - Response generation + fallback
- [ ] `console_ui.py` - Menu & user interface
- [ ] `chatbot.py` - Main orchestration logic
- [ ] `demo_script.py` - Testing & demo
- [ ] `requirements.txt` - All dependencies
- [ ] `README.md` - Setup & usage instructions
- [ ] **Demo Video** - 2-3 min showing all features
- [ ] `context.md` - This project context document

### Optional Bonuses:
- [ ] `src/voice_handler.py` - STT/TTS support
- [ ] `web_ui.py` - Web interface (Flask/FastAPI)
- [ ] `tests/test_*.py` - Unit tests

---

## 🔗 Useful Resources

### Bangla NLP
- [Bengali NLP Tools](https://github.com/csebuetnlp/BanglaNLP)
- [NormalizeBangla](https://github.com/msalim/NormalizeBangla)

### RAG & Semantic Search
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS Documentation](https://faiss.ai/)
- [RAG Tutorial](https://huggingface.co/course/chapter7)

### Bangla Voice
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs/languages)
- [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)

### Tools
- [JSON Validator](https://jsonlint.com/)
- [Unicode Bangla Checker](https://www.sslwireless.com/unicode_bangla.html)

---

## 📌 Notes & Tips

1. **Bangla Encoding**: Always save files with UTF-8 encoding
2. **Semantic Search**: Use multilingual models for better Bangla support
3. **Testing**: Test with various Bangla text styles (formal, informal)
4. **Fallback Message**: Make it friendly and encouraging
5. **FAQ Quality**: More specific keywords = better matching
6. **Performance**: Cache embeddings for faster retrieval
7. **Voice Quality**: Use professional TTS models for better pronunciation

---

## 🎓 Learning Outcomes

After completing this project, you will understand:
- ✅ RAG (Retrieval-Augmented Generation) pipeline
- ✅ Semantic search & embedding-based retrieval
- ✅ Metadata filtering for narrowed results
- ✅ Bangla NLP & Unicode handling
- ✅ Chatbot design & conversation flow
- ✅ (Bonus) Voice interface development
- ✅ Testing & demo creation

---

**Last Updated**: January 22, 2026  
**Status**: Ready for Implementation

"""Quick start guide and API documentation"""

# Bangla FAQ Chatbot - Usage Guide

## 🚀 Quick Start

### 1. Run the Interactive Chatbot
```bash
python3 main.py
```

### 2. Run the Demo
```bash
python3 demo_script.py
```

### 3. Run Tests
```bash
python3 -m unittest tests/test_components.py -v
```

---

## 📖 API Documentation

### Main Classes

#### BanglaFAQChatbot
Main chatbot orchestration class.

```python
from src.chatbot import BanglaFAQChatbot

# Initialize
chatbot = BanglaFAQChatbot('data/bangla_faqs.json')

# Generate answer
response, is_fallback = chatbot.generate_answer(
    query="পড়াশোনা",
    topic="শিক্ষা",
    difficulty=None  # Optional
)

# Get statistics
stats = chatbot.get_stats()

# Search similar
similar = chatbot.search_similar("AI", top_k=3)
```

#### FAQRetriever
Handles FAQ database and semantic search.

```python
from src.faq_retriever import FAQRetriever

retriever = FAQRetriever('data/bangla_faqs.json')

# Get all FAQs
all_faqs = retriever.get_all_faqs()

# Retrieve relevant FAQs
results = retriever.retrieve(
    query="পড়াশোনা",
    top_k=3
)

# Get by ID
faq = retriever.get_faq_by_id('edu_001')
```

#### MetadataFilter
Filter FAQs by metadata.

```python
from src.metadata_filter import MetadataFilter

# Filter by topic
filtered = MetadataFilter.filter_by_topic(faqs, "শিক্ষা")

# Filter by difficulty
filtered = MetadataFilter.filter_by_difficulty(faqs, "কঠিন")

# Apply multiple filters
filtered = MetadataFilter.apply_filters(
    faqs,
    topic="শিক্ষা",
    difficulty="মাঝারি"
)

# Get valid topics
topics = MetadataFilter.get_topics()
```

#### BanglaProcessor
Process and normalize Bangla text.

```python
from src.bangla_processor import BanglaProcessor

# Normalize text
normalized = BanglaProcessor.normalize("বাংলা   ভাষা")

# Tokenize
tokens = BanglaProcessor.tokenize("বাংলা ভাষা খুবই সুন্দর")

# Remove stop words
filtered = BanglaProcessor.remove_stopwords(tokens)

# Extract keywords
keywords = BanglaProcessor.extract_keywords(text, top_n=5)

# Calculate similarity
similarity = BanglaProcessor.calculate_similarity(text1, text2)
```

#### ResponseGenerator
Generate responses from FAQ matches.

```python
from src.response_generator import ResponseGenerator

# Generate response
response = ResponseGenerator.generate_response(
    faq_match=(faq_dict, score),
    include_metadata=True
)

# Get fallback
fallback = ResponseGenerator.get_fallback_response(topic="শিক্ষা")

# Format with context
formatted = ResponseGenerator.format_response_with_context(
    response_text="উত্তর",
    topic="শিক্ষা",
    difficulty="কঠিন",
    confidence=0.85,
    is_fallback=False
)
```

#### VoiceHandler (Bonus)
Handle voice input/output.

```python
from src.voice_handler import VoiceHandler

voice = VoiceHandler(language='bn')

# Text to speech
voice.speak("স্বাগতম চ্যাটবটে")

# Speech to text (requires microphone)
text = voice.recognize()

# Interactive mode
voice.interactive_mode()

# Check dependencies
deps = VoiceHandler.check_dependencies()
```

---

## 🎯 Common Use Cases

### Use Case 1: Simple Question Answering
```python
from src.chatbot import BanglaFAQChatbot

chatbot = BanglaFAQChatbot('data/bangla_faqs.json')

response, is_fallback = chatbot.generate_answer(
    "পড়াশোনায় মনোযোগ বাড়ানোর উপায়?",
    topic="শিক্ষা"
)

print(response)
```

### Use Case 2: Filtered Search
```python
response, is_fallback = chatbot.generate_answer(
    "কঠিন গণিত সমস্যা",
    topic="শিক্ষা",
    difficulty="কঠিন"
)
```

### Use Case 3: Multiple Results
```python
results, is_fallback = chatbot.answer_question(
    query="স্বাস্থ্য সমস্যা",
    topic="স্বাস্থ্য",
    return_multiple=True,
    top_k=3
)
```

### Use Case 4: Custom FAQ Loading
```python
from src.faq_retriever import FAQRetriever
from src.metadata_filter import MetadataFilter

retriever = FAQRetriever('data/bangla_faqs.json')
all_faqs = retriever.get_all_faqs()

# Filter for specific topic
education_faqs = MetadataFilter.filter_by_topic(all_faqs, "শিক্ষা")

# Retrieve
results = retriever.retrieve(
    "অনলাইন শিক্ষা",
    candidates=education_faqs,
    top_k=1
)
```

---

## ⚙️ Configuration

### Change Confidence Threshold
```python
from src.chatbot import BanglaFAQChatbot

BanglaFAQChatbot.CONFIDENCE_THRESHOLD = 0.2  # More strict
```

### Add Custom Fallback Messages
```python
from src.response_generator import ResponseGenerator

ResponseGenerator.FALLBACK_MESSAGES['শিক্ষা'] = "আমার কাছে এই তথ্য নেই।"
```

### Adjust Text Processing
```python
from src.bangla_processor import BanglaProcessor

# Add custom stop words
BanglaProcessor.STOP_WORDS.add('নতুন_শব্দ')

# Remove stop word
BanglaProcessor.STOP_WORDS.discard('এবং')
```

---

## 🧪 Testing

### Run All Tests
```bash
python3 -m unittest discover tests/ -v
```

### Run Specific Test
```bash
python3 -m unittest tests.test_components.TestBanglaProcessor -v
```

### Test with Coverage
```bash
pip install coverage
coverage run -m unittest discover tests/
coverage report
```

---

## 📊 FAQ Database Format

Each FAQ in `data/bangla_faqs.json` should follow:
```json
{
  "id": "unique_id",
  "topic": "শিক্ষা|স্বাস্থ্য|ভ্রমণ|প্রযুক্তি|খেলাধুলা",
  "difficulty": "সহজ|মাঝারি|কঠিন",
  "question": "প্রশ্ন বাংলায়",
  "answer": "উত্তর বাংলায়",
  "keywords": ["কীওয়ার্ড1", "কীওয়ার্ড2"],
  "tags": ["ট্যাগ1", "ট্যাগ2"]
}
```

---

## 🐛 Debugging

### Enable Verbose Output
```python
import logging

logging.basicConfig(level=logging.DEBUG)

chatbot = BanglaFAQChatbot('data/bangla_faqs.json')
```

### Check FAQ Loading
```python
chatbot = BanglaFAQChatbot('data/bangla_faqs.json')
print(f"Total FAQs: {chatbot.retriever.get_faq_count()}")
print(f"Topics: {chatbot.filter.get_topics()}")
```

### Test Retrieval
```python
from src.faq_retriever import FAQRetriever

retriever = FAQRetriever('data/bangla_faqs.json')
results = retriever.retrieve("পড়াশোনা", top_k=5)

for faq, score in results:
    print(f"Q: {faq['question']}")
    print(f"Score: {score:.2f}\n")
```

---

## 🔗 Integration Examples

### Flask Web API
```python
from flask import Flask, request, jsonify
from src.chatbot import BanglaFAQChatbot

app = Flask(__name__)
chatbot = BanglaFAQChatbot('data/bangla_faqs.json')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query')
    topic = data.get('topic')
    
    response, is_fallback = chatbot.generate_answer(query, topic)
    
    return jsonify({
        'response': response,
        'is_fallback': is_fallback
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Telegram Bot
```python
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from src.chatbot import BanglaFAQChatbot

chatbot = BanglaFAQChatbot('data/bangla_faqs.json')

async def handle_message(update: Update, context):
    text = update.message.text
    response, _ = chatbot.generate_answer(text, topic="শিক্ষা")
    await update.message.reply_text(response)

# Setup bot...
```

---

## 💡 Tips & Best Practices

1. **Use Specific Queries**: More specific queries get better matches
2. **Add More FAQs**: Improve coverage by adding more FAQ entries
3. **Tune Threshold**: Adjust confidence threshold based on needs
4. **Cache Results**: For production, cache FAQ embeddings
5. **Monitor Fallbacks**: Track when fallback responses are used
6. **Update Keywords**: Ensure FAQ keywords are relevant

---

## 📚 References

- [Bengali Unicode](https://en.wikipedia.org/wiki/Bengali_(script))
- [RAG Concepts](https://huggingface.co/course/chapter7)
- [Similarity Metrics](https://en.wikipedia.org/wiki/Jaccard_index)

---

**Last Updated:** January 22, 2026
**Version:** 1.0.0

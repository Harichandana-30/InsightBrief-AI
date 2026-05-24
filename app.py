import streamlit as st
from textblob import TextBlob
from collections import Counter
import re

st.title("📰 InsightBrief AI")
st.subheader("AI-Powered News Summarizer")

news_text = st.text_area(
    "Paste your news article here:",
    height=300
)

# Summarization
def summarize_text(text):
    sentences = text.split(". ")

    if len(sentences) > 3:
        summary = ". ".join(sentences[:3])
    else:
        summary = text

    return summary


# Sentiment Analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "😊 Positive"
    elif polarity < 0:
        return "😟 Negative"
    else:
        return "😐 Neutral"


# Category Detection
def detect_category(text):

    text = text.lower()

    if any(word in text for word in ["ai", "technology", "software", "computer", "internet"]):
        return "💻 Technology"

    elif any(word in text for word in ["match", "football", "cricket", "player", "tournament"]):
        return "⚽ Sports"

    elif any(word in text for word in ["government", "election", "minister", "politics"]):
        return "🏛 Politics"

    elif any(word in text for word in ["stock", "market", "finance", "business", "economy"]):
        return "💰 Business"

    elif any(word in text for word in ["movie", "music", "actor", "film", "celebrity"]):
        return "🎬 Entertainment"

    else:
        return "📌 General"


# Keyword Extraction
def extract_keywords(text):

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    stop_words = {
        "the", "is", "in", "and", "to", "of", "a", "for",
        "on", "with", "that", "as", "are", "it", "this",
        "by", "an", "be", "from", "at", "or"
    }

    filtered_words = [
        word for word in words
        if word not in stop_words and len(word) > 3
    ]

    word_counts = Counter(filtered_words)

    keywords = [
        word for word, count in word_counts.most_common(5)
    ]

    return keywords


if st.button("Generate Summary"):

    if news_text:

        summary = summarize_text(news_text)
        sentiment = get_sentiment(news_text)
        category = detect_category(news_text)
        keywords = extract_keywords(news_text)

        st.subheader("📌 Summary")
        st.write(summary)

        st.subheader("📊 Sentiment")
        st.write(sentiment)

        st.subheader("📰 Category")
        st.write(category)

        st.subheader("🔑 Keywords")
        st.write(", ".join(keywords))

    else:
        st.warning("Please paste a news article.")
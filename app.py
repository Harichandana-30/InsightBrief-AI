import streamlit as st
from textblob import TextBlob

st.title("📰 InsightBrief AI")
st.subheader("AI-Powered News Summarizer")

news_text = st.text_area(
    "Paste your news article here:",
    height=300
)

# Simple summarization function
def summarize_text(text):
    sentences = text.split(". ")

    if len(sentences) > 3:
        summary = ". ".join(sentences[:3])
    else:
        summary = text

    return summary

# Sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "😊 Positive"
    elif polarity < 0:
        return "😟 Negative"
    else:
        return "😐 Neutral"


if st.button("Generate Summary"):

    if news_text:

        summary = summarize_text(news_text)
        sentiment = get_sentiment(news_text)

        st.subheader("📌 Summary")
        st.write(summary)

        st.subheader("📊 Sentiment")
        st.write(sentiment)

    else:
        st.warning("Please paste a news article.")
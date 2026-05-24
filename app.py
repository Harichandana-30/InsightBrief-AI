import streamlit as st

st.title("📰 InsightBrief AI")

st.subheader("AI-Powered News Summarizer")

news_text = st.text_area(
    "Paste your news article here:",
    height=300
)

if st.button("Generate Summary"):
    if news_text:
        st.success("Article received successfully!")
    else:
        st.warning("Please paste a news article.")
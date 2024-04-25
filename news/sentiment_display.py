import streamlit as st
import pandas as pd

def display_sentiment_scores_dropdown(displayed_news):

    if displayed_news:
        st.header("Sentiment Analysis Scores")
        selected_article = st.selectbox("Select Article", [f"Article {i + 1}" for i in range(len(displayed_news))])

        if selected_article:
            index = int(selected_article.split()[-1]) - 1
            selected_news = displayed_news[index]
            sentiment = selected_news['sentiment']

            # Determine font color based on sentiment score
            font_color = '#AFE1AF' if sentiment['score'] > 0 else '#ff9999' if sentiment['score'] < 0 else '#FCFBF4'

            # Display sentiment analysis with font color using HTML
            st.write(f"Sentiment Analysis for {selected_article}:")
            st.markdown(
                f"<table><tr><th style='color: #FCFBF4;'>Sentiment</th><th style='color: #FCFBF4;'>Score</th></tr>"
                f"<tr><td style='color: {font_color};'>{sentiment['label'].capitalize()}</td>"
                f"<td style='color: {font_color};'>{sentiment['score']}</td></tr></table>",
                unsafe_allow_html=True
            )


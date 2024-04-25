# # col_2_news.py

import streamlit as st
import requests
import nltk
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import logging
import pandas as pd
import matplotlib.pyplot as plt
from news.sentiment_analysis import analyze_sentiment
from news.news_scraper import scrape_general_news
from stocks.stock_lists import all_stocks
from news.sentiment_plotting import plot_sentiment_scores
from news.news_custom_scraper import find_sentences_with_keywords, scrape_custom_news_with_keywords
from news.sentiment_display import display_sentiment_scores_dropdown, display_text_count_dropdown

# Your Finnhub API key
API_KEY = 'cogmlnpr01qj0pq2pnk0cogmlnpr01qj0pq2pnkg'

def fetch_stock_news(symbol):
    """ Fetches the latest stock news for a given symbol from Finnhub API. """
    url = f'https://finnhub.io/api/v1/company-news?symbol={symbol}&from={pd.Timestamp.now().date()}&to={pd.Timestamp.now().date()}&token={API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def limit_sentences(text, max_sentences=3):
    sentences = text.split(".")
    return ". ".join(sentences[:max_sentences]) + ("." if len(sentences) > 2 else "")

def display_news_bullet_points(news_list):
    for news in news_list[:6]:
        if 'summary' in news and news['summary']:
            limited_text = limit_sentences(news['summary'])
            st.markdown(f"- **[{news['headline']}]({news['url']})**: {limited_text}")


nltk.download('punkt')

def scrape_and_process_news():
    # Call the scraping function to get raw news data
    scraped_articles = scrape_general_news()

    # Process each article to analyze sentiment and score
    news_data = []
    for article in scraped_articles:
        # Analyze sentiment and get the score
        sentiment, score = analyze_sentiment(article['text'])

        # Add the sentiment score to the article dictionary
        article['score'] = score

        # Append the article dictionary to the news data list
        news_data.append(article)

    return news_data


def display_news_headlines(news_data):
    
    news_headlines = ""
    
    # Iterate over all news and use enumeration for correct indexing
    for index, news in enumerate(news_data):
        text = news['text']
        sentiment = analyze_sentiment(text)
        sentiment_label = sentiment['label']
        sentiment_score = sentiment['score']
        sentences = text.split('.')[:4]
        display_text = '.'.join(sentences) + '.'
        color = '#AFE1AF' if sentiment_label == 'positive' else '#ff9999' if sentiment_label == 'negative' else '#FCFBF4'
        news_headlines += f"<span style='color: {color};'>{index + 1}. {display_text}</span><br><br>"

    st.markdown(f"<div style='max-height: 400px; overflow-y: auto;'>{news_headlines}</div>", unsafe_allow_html=True)

def display_col2(selected_stock):
    st.header("Today's Global News")
    general_news = scrape_general_news()

    if general_news:
        display_news_headlines(general_news)
        st.markdown("<hr>", unsafe_allow_html=True)
        with st.expander("Sentiment Analysis"):
            
            #display_sentiment_analysis(general_news)
            display_sentiment_scores_dropdown(general_news)

        st.markdown("<hr>", unsafe_allow_html=True)

         # Expander for Article Ranking
        with st.expander("Article Ranking", expanded=False):
            sentiment_data = [{"Article Number": i + 1, "Sentiment": article['sentiment']['label'], 
                               "Score": article['sentiment']['score']} for i, article in enumerate(general_news)]
            sentiment_df = pd.DataFrame(sentiment_data)
            
            # Sort sentiment_df by score in descending order
            sentiment_df = sentiment_df.sort_values(by='Score', ascending=False)
            st.table(sentiment_df)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
        with st.expander("Text Count"):
            display_text_count_dropdown(general_news)
    else:
        st.error("Failed to fetch general news.")



    st.markdown("<hr>", unsafe_allow_html=True)
    
    if selected_stock:
        st.header(f"News for {selected_stock}")
        stock_news = fetch_stock_news(selected_stock)

        if stock_news:
            display_news_bullet_points(stock_news)
        else:
            st.warning(f"No news found for {selected_stock}.")
    else:
        st.warning("No stock selected.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Scrape Custom URL with Keywords")
    custom_url = st.text_input("Enter URL to scrape:")
    keywords = st.text_input("Enter keywords (comma-separated):")

    if st.button("Scrape"):
        if custom_url:
            custom_news = scrape_custom_news_with_keywords(custom_url, keywords)
            if custom_news:
                st.write("Scraped Text:")
                for news in custom_news[:3]:  # Limit to maximum 3 articles
                    sentences = find_sentences_with_keywords(news['text'], keywords)
                    for sentence in sentences:
                        st.markdown(f"- {sentence}")  # Display each sentence as a bullet point
            else:
                st.warning("Failed to scrape custom news.")
        else:
            st.warning("Please enter a URL to scrape.")

    
    st.markdown("<hr>", unsafe_allow_html=True)








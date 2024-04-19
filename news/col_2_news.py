
# col_2_news.py

import requests
import pandas as pd
import streamlit as st
from news.sentiment_analysis import analyze_sentiment
from news.news_scraper import scrape_general_news, scrape_stock_news
from stocks.stock_lists import all_stocks, all_indices
from news.news_custom_scraper import scrape_custom_news, scrape_custom_news_with_keywords, find_sentences_with_keywords


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
    for news in news_list[:6]:  # Displaying only the first 6 news items
        if 'summary' in news and news['summary']:  # Check if summary exists and is not empty
            limited_text = limit_sentences(news['summary'])
            st.markdown(f"- **[{news['headline']}]({news['url']})**: {limited_text}")

def display_col2(selected_stock):
    st.header("Today's Global News")

    # Function to limit the text to the first 3 sentences
    def limit_sentences1(text, max_sentences=3):
        sentences = text.split(".")
        return ". ".join(sentences[:max_sentences]) + ("." if len(sentences) > 2 else "")

    # Function to display news articles in bullet points, each limited to 3 sentences

    def display_news_bullet_points1(news_list):

        for i, news in enumerate(news_list[:6]):  # Limit to maximum 6 bullet points
            sentiment = analyze_sentiment(news['text'])
            color = "#ADD8E6" if sentiment == "positive" else "#F08080" if sentiment == "negative" else "#D3D3D3"
            limited_text = limit_sentences1(news['text'])
            st.markdown(f"- <p style='color: {color};'> {limited_text}</p>", unsafe_allow_html=True)

    
    # Scrape and display general news for all stocks in bullet points
    general_news = scrape_general_news()

    if general_news:
        display_news_bullet_points1(general_news)
    else:
        st.warning("Failed to fetch general news.")

    # Add a horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # Display news specific to the selected stock in bullet points, limited to 3 sentences each
    if selected_stock:
        st.header(f"News for {selected_stock}")
        stock_news = fetch_stock_news(selected_stock)

        if stock_news:
            display_news_bullet_points(stock_news)

        else:
            st.warning(f"No news found for {selected_stock}.")
    else:
        st.warning("No stock selected.")

     # Add a horizontal divider
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

    # st.subheader("Scrape Custom URL with Keywords")
    # custom_url = st.text_input("Enter URL to scrape:")
    # keywords = st.text_input("Enter keywords (comma-separated):")

    # if st.button("Scrape"):
    #     if custom_url:
    #         custom_news = scrape_custom_news_with_keywords(custom_url, keywords)
    #         if custom_news:
    #             st.write("Scraped Text:")
    #             for news in custom_news:
    #                 st.write(news['text'])
    #         else:
    #             st.warning("Failed to scrape custom news.")
    #     else:
    #         st.warning("Please enter a URL to scrape.")
    # else:
    #     st.warning("No stock selected.")





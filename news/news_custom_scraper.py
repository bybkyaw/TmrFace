# news_custom_scraper.py

import logging
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from news.sentiment_analysis import analyze_sentiment


def scrape_custom_news(custom_url):
    scraped_data = []
    
    try:
        response = requests.get(custom_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article')  # Adjust this based on the HTML structure of the website
            if articles:
                for article in articles:
                    article_text = article.get_text()
                    sentiment = analyze_sentiment(article_text)
                    scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "Custom"})
        else:
            logging.warning(f"Failed to fetch news from {custom_url}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error scraping news: {e}")
    return scraped_data


def scrape_custom_news_with_keywords(custom_url, keywords):
    scraped_data = []
    
    try:
        response = requests.get(custom_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article')  # Adjust this based on the HTML structure of the website
            if articles:
                for article in articles:
                    article_text = article.get_text()
                    if any(keyword.strip().lower() in article_text.lower() for keyword in keywords.split(',')):
                        sentiment = analyze_sentiment(article_text)
                        scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "Custom"})
        else:
            logging.warning(f"Failed to fetch news from {custom_url}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error scraping news from {custom_url}: {e}")
    return scraped_data



# def scrape_custom_news_with_keywords(custom_url, keywords):
#     scraped_data = []
    
#     try:
#         response = requests.get(custom_url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             articles = soup.find_all('article')  # Adjust this based on the HTML structure of the website
#             if articles:
#                 for article in articles:
#                     article_text = article.get_text()
#                     if any(keyword.strip().lower() in article_text.lower() for keyword in keywords.split(',')):
#                         sentiment = analyze_sentiment(article_text)
#                         scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "Custom"})
#         else:
#             logging.warning(f"Failed to fetch news from {custom_url}. Status code: {response.status_code}")
#     except Exception as e:
#         logging.error(f"Error scraping news: {e}")
#     return scraped_data

# news_custom_scraper.py

import logging
import requests
import nltk
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
from textblob import TextBlob
from news.sentiment_analysis import analyze_sentiment


def scrape_custom_news(custom_url):
    scraped_data = []
    
    try:
        response = requests.get(custom_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article')  
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
            articles = soup.find_all('article')  
            if articles:
                for article in articles:
                    article_text = article.get_text()
                    article_lower = article_text.lower()

                    # Check if any of the keywords are present in the article text
                    if any(keyword.strip().lower() in article_lower for keyword in keywords.split(',')):
                        sentiment = analyze_sentiment(article_text)
                        scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "Custom"})
        else:
            logging.warning(f"Failed to fetch news from {custom_url}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error scraping news from {custom_url}: {e}")
    return scraped_data


nltk.download('punkt')

def find_sentences_with_keywords(text, keywords, max_instances=3):
    sentences = sent_tokenize(text)
    matching_sentences = []
    for sentence in sentences:
        if any(keyword.strip().lower() in sentence.lower() for keyword in keywords.split(',')):
            matching_sentences.append(sentence)
            if len(matching_sentences) >= max_instances:
                break
    return matching_sentences


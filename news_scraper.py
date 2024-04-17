import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import logging
from news_urls import general_news_urls, financial_news_urls


# Function to scrape general news for all stocks and finance news
def scrape_general_news():
    scraped_data = []
    try:
        # Scrape general news for all stocks
        for url in general_news_urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('article')  # Adjust this based on the HTML structure of the websites
                if articles:
                    for article in articles:
                        article_text = article.get_text()
                        sentiment = analyze_sentiment(article_text)
                        scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "General"})
            else:
                logging.warning(f"Failed to fetch news from {url}. Status code: {response.status_code}")

        # Scrape finance news
        for url in financial_news_urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('article')  # Adjust this based on the HTML structure of the websites
                if articles:
                    for article in articles:
                        article_text = article.get_text()
                        sentiment = analyze_sentiment(article_text)
                        scraped_data.append({"text": article_text, "sentiment": sentiment, "source": "Finance"})
            else:
                logging.warning(f"Failed to fetch news from {url}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error scraping news: {e}")
    return scraped_data


# Function to scrape news specific to a selected stock
def scrape_stock_news(selected_stock):
    news_headlines = []
    try:
        url = financial_news_urls.get(selected_stock)
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                headlines = soup.find_all("h3", {"class": "Mb(5px)"})
                for headline in headlines:
                    text = headline.text.strip()
                    analysis = TextBlob(text)
                    sentiment = "neutral"
                    if analysis.sentiment.polarity > 0.1:  # Threshold for positive sentiment
                        sentiment = "positive"
                    elif analysis.sentiment.polarity < -0.1:  # Threshold for negative sentiment
                        sentiment = "negative"
                    news_headlines.append({'text': text, 'sentiment': sentiment})
            else:
                logging.warning(f"Failed to fetch news for {selected_stock}. Status code: {response.status_code}")
        else:
            logging.warning(f"No URL found for {selected_stock}.")
    except Exception as e:
        logging.error(f"Error scraping news for {selected_stock}: {e}")
    return news_headlines


# Function for sentiment analysis
def analyze_sentiment(text):
    if text:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            return "positive"
        elif sentiment_score < 0:
            return "negative"
        else:
            return "neutral"
    else:
        return None



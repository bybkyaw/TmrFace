#sentiment_analysis.py

from textblob import TextBlob

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
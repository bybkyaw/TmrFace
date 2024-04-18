#sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(text):

    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "positive"
    
    elif blob.sentiment.polarity < 0:
        return "negative"
    
    else:
        return "neutral"

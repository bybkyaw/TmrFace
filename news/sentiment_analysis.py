#sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return {"label": "positive", "score": sentiment_score}
    elif sentiment_score < 0:
        return {"label": "negative", "score": sentiment_score}
    else:
        return {"label": "neutral", "score": sentiment_score}


def analyze_sentiment_and_score(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive", polarity
    elif polarity < 0:
        return "negative", polarity
    else:
        return "neutral", 0

# #sentiment_analysis.py

# from textblob import TextBlob

# def analyze_sentiment(text):

#     blob = TextBlob(text)
#     if blob.sentiment.polarity > 0:
#         return "positive"
    
#     elif blob.sentiment.polarity < 0:
#         return "negative"
    
#     else:
#         return "neutral"

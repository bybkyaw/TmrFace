import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_scores(news_data):

    # Create a DataFrame from the news data
    df = pd.DataFrame(news_data)

    # Plot scatter plot of sentiment scores
    plt.figure(figsize=(10, 6))
    plt.scatter(range(1, len(df) + 1), df['score'], color='blue')
    plt.title("Sentiment Rating Scores of Articles")
    plt.xlabel("Article Number")
    plt.ylabel("Sentiment Score")
    plt.grid(True)
    return plt


def plot_sentiment_scores(sentiment_scores):

    plt.figure(figsize=(10, 6))
    plt.scatter(range(1, len(sentiment_scores) + 1), sentiment_scores, color='blue')
    plt.title("Sentiment Scores of Articles")
    plt.xlabel("Article Number")
    plt.ylabel("Sentiment Score")
    plt.grid(True)

    return plt

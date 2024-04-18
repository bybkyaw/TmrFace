# col_2_news.py

import streamlit as st
from news_scraper import scrape_general_news, scrape_stock_news
from news_custom_scraper import scrape_custom_news, scrape_custom_news_with_keywords

# Main function for column 2 - news
def display_col2(selected_stock):
    st.header("Today's Stock Market News")

    # Function to limit the text to the first 3 sentences
    def limit_sentences(text, max_sentences=3):
        sentences = text.split(".")
        return ". ".join(sentences[:max_sentences]) + ("." if len(sentences) > 2 else "")

    # Function to display news articles in bullet points, each limited to 3 sentences
    def display_news_bullet_points(news_list):
        for i, news in enumerate(news_list[:6]):  # Limit to maximum 6 bullet points
            limited_text = limit_sentences(news['text'])
            st.write(f"- {limited_text}")

    # Scrape and display general news for all stocks in bullet points
    general_news = scrape_general_news()
    if general_news:
        st.header("General News")
        display_news_bullet_points(general_news)
    else:
        st.warning("Failed to fetch general news.")

    # Add a horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # Display news specific to the selected stock in bullet points, limited to 3 sentences each
    if selected_stock:
        st.header(f"News for {selected_stock}")
        stock_news = scrape_stock_news(selected_stock)
        if stock_news:
            display_news_bullet_points(stock_news)
        else:
            st.warning(f"No news found for {selected_stock}.")

        # Add custom URL and keywords scraping functionality
        st.subheader("Scrape Custom URL with Keywords")
        custom_url = st.text_input("Enter URL to scrape:")
        keywords = st.text_input("Enter keywords (comma-separated):")
        if st.button("Scrape"):
            if custom_url:
                custom_news = scrape_custom_news_with_keywords(custom_url, keywords)
                if custom_news:
                    st.write("Scraped Text:")
                    for news in custom_news:
                        st.write(news['text'])
                else:
                    st.warning("Failed to scrape custom news.")
            else:
                st.warning("Please enter a URL to scrape.")
    else:
        st.warning("No stock selected.")



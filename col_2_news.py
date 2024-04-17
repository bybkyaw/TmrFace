import streamlit as st
from news_scraper import scrape_general_news, scrape_stock_news


# Main function for column 2 - news
def display_col2(selected_stock=None):
    st.header("Today's Stock Market News")

    # Function to limit the number of lines to display
    def limit_lines(text, max_lines=40):
        lines = text.split(".")
        lines = [line.strip() for line in lines if line.strip()]
        return lines[:max_lines]

    # Function to display lines without splitting
    def display_lines(lines):
        st.write("\n".join(lines))

    # Scrape and display general news for all stocks and finance news
    general_news = scrape_general_news()
    if general_news:
        st.header("General News")
        count = 0
        all_lines = []
        for article in general_news:
            if count >= 20:
                break
            text = article.get("text")
            sentiment = article.get("sentiment")
            source = article.get("source")
            lines = limit_lines(text)
            all_lines.extend(lines)
            count += len(lines)
        display_lines(all_lines)
    else:
        st.warning("Failed to fetch general news.")

    # Add a horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # st.header("Finance News")  # Title for the Finance News section

    # # Importing financial news URLs from news_urls.py
    # from news_urls import financial_news_urls
    #
    # # Display finance news
    # if financial_news_urls:
    #     count = 0
    #     all_lines = []
    #     for url in financial_news_urls:
    #         financial_news = scrape_general_news()
    #         if financial_news:
    #             for article in financial_news:
    #                 if count >= 20:
    #                     break
    #                 text = article.get("text")
    #                 sentiment = article.get("sentiment")
    #                 source = article.get("source")
    #                 lines = limit_lines(text)
    #                 all_lines.extend(lines)
    #                 count += len(lines)
    #         else:
    #             st.warning(f"Failed to fetch finance news from {url}.")
    #     display_lines(all_lines)
    # else:
    #     st.warning("No financial news URLs found.")
    #
    # # Add a horizontal divider
    # st.markdown("<hr>", unsafe_allow_html=True)

    st.header(f"News for {selected_stock}")
    # Display news specific to the selected stock
    if selected_stock:
        st.write(f"DEBUG: selected_stock: {selected_stock}")  # Debugging statement
        st.header(f"News for {selected_stock}")
        stock_news = scrape_stock_news(selected_stock)
        if stock_news:
            all_lines = []
            for news in stock_news:
                text = news.get("text")
                lines = limit_lines(text)
                all_lines.extend(lines)
            display_lines(all_lines)
        else:
            st.warning(f"No news found for {selected_stock}.")  # Display a warning if no news found
    else:
        st.warning("No stock selected.")  # Display a warning if no stock selected




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def display_sentiment_scores_dropdown(displayed_news):
    if displayed_news:
        st.header("Sentiment Analysis")
        selected_article = st.selectbox("Select Article", [f"Article {i + 1}" for i in range(len(displayed_news))])

        if selected_article:
            index = int(selected_article.split()[-1]) - 1
            selected_news = displayed_news[index]
            sentiment = selected_news['sentiment']

            # Determine dot color based on sentiment score
            dot_color = '#AFE1AF' if sentiment['score'] > 0 else '#ff9999' if sentiment['score'] < 0 else '#FCFBF4'

            # Display sentiment analysis with dot color using HTML
            st.write(f"Sentiment Analysis Score for {selected_article}:")
            st.markdown(
                f"<table><tr><th style='color: #FCFBF4;'>Sentiment</th><th style='color: #FCFBF4;'>Score</th></tr>"
                f"<tr><td style='color: {dot_color};'>{sentiment['label'].capitalize()}</td>"
                f"<td style='color: {dot_color};'>{sentiment['score']}</td></tr></table>",
                unsafe_allow_html=True
            )
        st.write("")
        
        # Checkbox to show/hide sentiment scores for all articles
        show_scores = st.checkbox("Show sentiment scores for all articles")

        if show_scores:
            # Display table of sentiment scores for all articles
            st.header("Sentiment Scores for All Articles")
            sentiment_data = [{"Article Number": i + 1, "Sentiment": article['sentiment']['label'], 
                               "Score": article['sentiment']['score']} for i, article in enumerate(displayed_news)]
            sentiment_df = pd.DataFrame(sentiment_data)
            st.table(sentiment_df)

        st.markdown("<hr>", unsafe_allow_html=True)

        # Display scatter plot for sentiment scores of all articles
        st.header("Scatter Plot for All Articles")
        all_sentiments = []
        for i, article in enumerate(displayed_news):
            all_sentiments.append({'Article Number': i + 1, 'Score': article['sentiment']['score'],
                                   'Color': 'Positive' if article['sentiment']['score'] > 0
                                            else 'Negative' if article['sentiment']['score'] < 0
                                            else 'Neutral'})
            
        all_sentiments_df = pd.DataFrame(all_sentiments)

        fig_scatter = px.scatter(all_sentiments_df, x='Article Number', y='Score', color='Color',
                                 title='Sentiment Analysis Scatter Plot',
                                 labels={'Article Number': 'Article Number', 'Score': 'Sentiment Score'},
                                 hover_name='Article Number', hover_data={'Score': True},
                                 render_mode='webgl')  
        
        fig_scatter.update_traces(mode='lines+markers', line=dict(color='#C0C0C0', width=1))  # Connect dots with lines
        fig_scatter.update_layout(hovermode='closest')  # Show closest data on hover
        st.plotly_chart(fig_scatter)

        st.write("")
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # # Expander to show/hide Article Ranking
        # with st.expander("Article Ranking", expanded=False):
        #     # Display table of sentiment scores for all articles
        #     sentiment_data = [{"Article Number": i + 1, "Sentiment": article['sentiment']['label'], 
        #                        "Score": article['sentiment']['score']} for i, article in enumerate(displayed_news)]
        #     sentiment_df = pd.DataFrame(sentiment_data)
            
        #     # Sort sentiment_df by score in descending order
        #     sentiment_df = sentiment_df.sort_values(by='Score', ascending=False)
        #     st.table(sentiment_df)

    else:
        st.warning("No sentiment scores found in the news data.")


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px


# def display_sentiment_scores_dropdown(displayed_news):
#     if displayed_news:
#         st.header("Sentiment Analysis")
#         selected_article = st.selectbox("Select Article", [f"Article {i + 1}" for i in range(len(displayed_news))])

#         if selected_article:
#             index = int(selected_article.split()[-1]) - 1
#             selected_news = displayed_news[index]
#             sentiment = selected_news['sentiment']

#             # Determine dot color based on sentiment score
#             dot_color = '#AFE1AF' if sentiment['score'] > 0 else '#ff9999' if sentiment['score'] < 0 else '#FCFBF4'

#             # Display sentiment analysis with dot color using HTML
#             st.write(f"Sentiment Analysis Score for {selected_article}:")
#             st.markdown(
#                 f"<table><tr><th style='color: #FCFBF4;'>Sentiment</th><th style='color: #FCFBF4;'>Score</th></tr>"
#                 f"<tr><td style='color: {dot_color};'>{sentiment['label'].capitalize()}</td>"
#                 f"<td style='color: {dot_color};'>{sentiment['score']}</td></tr></table>",
#                 unsafe_allow_html=True
#             )
#         st.write("")
#         # Checkbox to show/hide sentiment scores for all articles
#         show_scores = st.checkbox("Show sentiment scores for sll srticles")

#         if show_scores:
#             # Display table of sentiment scores for all articles
#             st.header("Sentiment Scores for All Articles")
#             sentiment_data = [{"Article Number": i + 1, "Sentiment": article['sentiment']['label'], 
#                                "Score": article['sentiment']['score']} for i, article in enumerate(displayed_news)]
#             sentiment_df = pd.DataFrame(sentiment_data)
#             st.table(sentiment_df)

#         st.markdown("<hr>", unsafe_allow_html=True)

#         # Display scatter plot for sentiment scores of all articles
#         st.header("Scatter Plot for All Articles")
#         all_sentiments = []
#         for i, article in enumerate(displayed_news):

#             all_sentiments.append({'Article Number': i + 1, 'Score': article['sentiment']['score'],
#                                    'Color': 'Positive' if article['sentiment']['score'] > 0
#                                             else 'Negative' if article['sentiment']['score'] < 0
#                                             else 'Neutral'})
            
#         all_sentiments_df = pd.DataFrame(all_sentiments)

#         fig_scatter = px.scatter(all_sentiments_df, x='Article Number', y='Score', color='Color',
#                                  title='Sentiment Analysis Scatter Plot',
#                                  labels={'Article Number': 'Article Number', 'Score': 'Sentiment Score'},
#                                  hover_name='Article Number', hover_data={'Score': True},
#                                  render_mode='webgl')  
        
#         fig_scatter.update_traces(mode='lines+markers', line=dict(color='#C0C0C0', width=1))  # Connect dots with lines
#         fig_scatter.update_layout(hovermode='closest')  # Show closest data on hover
#         st.plotly_chart(fig_scatter)

#         st.write("")
        
#         st.markdown("<hr>", unsafe_allow_html=True)
        
#         # Checkbox to show/hide Article Ranking
#         show_ranking = st.checkbox("Article Ranking")

#         if show_ranking:
#             # Display table of sentiment scores for all articles
#             st.header("Article Ranking")
#             sentiment_data = [{"Article Number": i + 1, "Sentiment": article['sentiment']['label'], 
#                                "Score": article['sentiment']['score']} for i, article in enumerate(displayed_news)]
#             sentiment_df = pd.DataFrame(sentiment_data)
            
#             # Sort sentiment_df by score in descending order
#             sentiment_df = sentiment_df.sort_values(by='Score', ascending=False)
#             st.table(sentiment_df)


#     else:
#         st.warning("No sentiment scores found in the news data.")





def display_text_count_dropdown(general_news):
    if general_news:
        st.header("Scrapped Articles Text Count")
        
        # Create a list to hold text count data for each article
        text_count_data = []

        # Iterate over each article in general_news
        for index, article in enumerate(general_news):

            # Count the number of words in the article's text
            text_count = len(article['text'].split())
            # Append article number and text count to the list

            text_count_data.append({"Article Number": index + 1, "Text Count": text_count})

        # Create a DataFrame from the text count data
        text_count_df = pd.DataFrame(text_count_data)

        # Display the text count data in a table format
        st.table(text_count_df)

        # Plot the text count data as a hoverable bar chart using Plotly Express
        fig = px.bar(text_count_df, x='Article Number', y='Text Count', 
                     title='Text Count for Each Article',
                     labels={'Article Number': 'Article Number', 'Text Count': 'Text Count'})
        fig.update_layout(xaxis=dict(type='category'))  # Ensure article number is treated as category
        st.plotly_chart(fig)

    else:
        st.warning("No articles available.")




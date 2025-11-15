import streamlit as st
from gnews import GNews

# Set page config
st.set_page_config(page_title="Live Sector News", page_icon="📰")

# Use custom CSS for light green background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e8f5e9;  /* light green */
    }
    .sector-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .news-item {
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📊 Live News by Sector")

# Initialize GNews
gn = GNews(language='en', country='US')

# Define your sectors and corresponding Google News topics or queries
sectors = {
    "Business": "BUSINESS",
    "Technology": "TECHNOLOGY",
    "Health": "HEALTH",
    "Sports": "SPORTS",
    "Entertainment": "ENTERTAINMENT",
}

# For each sector, fetch top news
for sector_name, topic in sectors.items():
    st.markdown(f"<div class='sector-title'>{sector_name}</div>", unsafe_allow_html=True)
    try:
        articles = gn.get_news(topic)  # returns a list of news dicts
    except Exception as e:
        st.error(f"Error getting {sector_name} news: {e}")
        continue

    # Display top 5 articles for each
    for article in articles[:5]:
        # article keys: "title", "publisher", "published date", "url", "description"
        title = article.get("title")
        source = article.get("publisher")
        date = article.get("published date")
        link = article.get("url")
        desc = article.get("description")

        st.markdown(
            f"""
            <div class="news-item">
            <a href="{link}" target="_blank"><strong>{title}</strong></a><br>
            <small>{source} — {date}</small><br>
            <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

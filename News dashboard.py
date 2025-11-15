import streamlit as st
import feedparser

st.set_page_config(page_title="Live News - 5 Sectors", layout="wide")

st.markdown("""
    <h2 style='color:black;'>Live News From 5 Sectors (Times of India)</h2>
""", unsafe_allow_html=True)

# --- Light Green Background CSS ---
st.markdown("""
    <style>
        .news-box {
            background-color: #ccffcc;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Times of India RSS Feeds (Public) ---
RSS_FEEDS = {
    "Business": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    "Sports": "https://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
    "Technology": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "Entertainment": "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    "World": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"
}

# --- Display each sector ---
for sector, url in RSS_FEEDS.items():
    st.subheader(f"🟢 {sector} News")
    feed = feedparser.parse(url)

    for entry in feed.entries[:5]:  # Show top 5 headlines per sector
        st.markdown(f"""
            <div class="news-box">
                <h4>{entry.title}</h4>
                <a href="{entry.link}" target="_blank">Read more</a>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")

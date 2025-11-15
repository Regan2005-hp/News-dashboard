import streamlit as st
import feedparser
import time

st.set_page_config(page_title="Live News Dashboard", layout="wide")

# ------------------- CSS for UI -------------------
st.markdown("""
<style>
    .news-card {
        background-color: #ccffcc;
        padding: 15px;
        margin: 10px 0px;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }
    .news-title {
        font-size: 18px;
        font-weight: bold;
    }
    .news-desc {
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ------------------- RSS FEEDS -------------------
RSS_FEEDS = {
    "Business": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    "Sports": "https://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
    "Technology": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "Entertainment": "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    "World": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
    "Health": "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    "Education": "https://timesofindia.indiatimes.com/rssfeeds/913168846.cms",
    "India": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "Finance": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms"
}

# ------------------- Sidebar Options -------------------
st.sidebar.title("⚙️ Settings")

refresh_time = st.sidebar.slider("Auto-refresh time (seconds)", 10, 120, 30)

sector = st.sidebar.selectbox("Choose News Sector", list(RSS_FEEDS.keys()))

st.title(f"📰 Live News: {sector}")

# ------------------- Auto Refresh -------------------
placeholder = st.empty()

while True:
    with placeholder.container():
        feed = feedparser.parse(RSS_FEEDS[sector])

        for entry in feed.entries[:6]:      # Show top 6 news
            image = entry.media_thumbnail[0]['url'] if "media_thumbnail" in entry else ""

            st.markdown(f"""
                <div class="news-card">
                    <div class="news-title">{entry.title}</div>
                    <br>
                    <div class="news-desc">
                        <a href="{entry.link}" target="_blank">Read Full Article</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    time.sleep(refresh_time)


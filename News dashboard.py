import streamlit as st
import requests

# ---------------------------
# PAGE CONFIG + BACKGROUND
# ---------------------------
st.set_page_config(page_title="Live Sector News", layout="wide")

page_bg = """
<style>
body {
    background-color: #e6ffe6; /* light green */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("📰 Live News from 5 Sectors")
st.write("Automatically updates each time you refresh!")

# ---------------------------
# NEWS API FUNCTION
# ---------------------------
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(category):
    params = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data.get("articles", [])

# ---------------------------
# SECTORS
# ---------------------------
sectors = {
    "Technology": "technology",
    "Finance": "business",
    "Sports": "sports",
    "Health": "health",
    "Entertainment": "entertainment"
}

# ---------------------------
# DISPLAY NEWS
# ---------------------------
for sector_title, api_name in sectors.items():
    st.subheader(f"📌 {sector_title} News")

    articles = get_news(api_name)

    if not articles:
        st.write("No news available at the moment.")
        continue

    for article in articles[:5]:  # 5 top headlines per sector
        st.markdown(f"### 🔸 {article['title']}")
        if article.get("description"):
            st.write(article["description"])
        if article.get("url"):
            st.markdown(f"[Read more]({article['url']})")
        st.write("---")

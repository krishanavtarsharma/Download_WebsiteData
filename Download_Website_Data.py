import streamlit as st
import requests
from bs4 import BeautifulSoup

# Page configuration
st.set_page_config(page_title="Website HTML Downloader", layout="centered")
st.title("🌐 Website HTML Downloader")

# User input
url = st.text_input("🔗 Enter Website URL (e.g. https://example.com)")

# Button to trigger download
if st.button("📄 Download HTML"):
    if not url.startswith("http"):
        st.warning("⚠️ Please enter a valid URL with http or https.")
    else:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            html_content = soup.prettify()

            # Display HTML
            st.text_area("🧾 Website HTML Content", html_content, height=400)

            # Optional: Download as file
            st.download_button(
                label="⬇️ Download as HTML file",
                data=html_content,
                file_name="website_data.html",
                mime="text/html"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")

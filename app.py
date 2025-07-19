"""
PhishGuard – URL & QR Phishing Detector
Single-file Streamlit application
"""

import os
import io
import streamlit as st
import validators
import requests
from pyzbar.pyzbar import decode as qr_decode
from PIL import Image

###############################################################################
# Page config
###############################################################################
st.set_page_config(
    page_title="PhishGuard – URL & QR Phishing Detector",
    page_icon="🛡️",
    layout="centered",
)

###############################################################################
# Globals
###############################################################################
API_KEY = os.getenv("GSB_API_KEY")  # Never log this
GSB_ENDPOINT = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
CLIENT_ID = "PhishGuard"
CLIENT_VERSION = "1.0.0"

###############################################################################
# Sidebar
###############################################################################
with st.sidebar:
    st.title("How it works")
    st.markdown(
        """
1. **Paste** any URL or **upload** a QR code image.  
2. PhishGuard checks the link with Google Safe Browsing.  
3. You instantly see **✅ Safe** or **🚨 Phishing Detected**.
        """
    )
    st.info(
        "To run locally, set the env var `GSB_API_KEY` to your Google Safe Browsing key."
    )
    st.markdown(
        "[📦 GitHub repo](https://github.com/yourname/phishguard)",
        unsafe_allow_html=True,
    )

###############################################################################
# Helper functions
###############################################################################
@st.cache_data(show_spinner=False)
def call_gsb(url: str) -> dict:
    """Return GSB threatMatches JSON or {} on error."""
    if not API_KEY:
        st.error("Missing GSB_API_KEY environment variable.")
        return {}
    payload = {
        "client": {"clientId": CLIENT_ID, "clientVersion": CLIENT_VERSION},
        "threatInfo": {
            "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    try:
        r = requests.post(
            f"{GSB_ENDPOINT}?key={API_KEY}",
            json=payload,
            timeout=5,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"Network/API error: {e}")
        return {}


def classify_url(url: str) -> tuple[str, list[str]]:
    """Return ('SAFE', []) or ('UNSAFE', [threat, …])."""
    if not validators.url(url):
        return ("INVALID", [])
    resp = call_gsb(url)
    matches = resp.get("matches", [])
    if matches:
        threats = [m["threatType"] for m in matches]
        return ("UNSAFE", threats)
    return ("SAFE", [])


def extract_url_from_qr(img_bytes):
    """Return decoded URL or None."""
    try:
        img = Image.open(io.BytesIO(img_bytes))
        decoded = qr_decode(img)
        for obj in decoded:
            data = obj.data.decode("utf-8").strip()
            if validators.url(data):
                return data
    except Exception as e:
        st.error(f"QR decode error: {e}")
    return None

###############################################################################
# Main UI
###############################################################################
st.title("🛡️ PhishGuard")
st.caption("Detect phishing links from URLs or QR codes in seconds")

tab_url, tab_qr = st.tabs(["🔗 Paste URL", "📷 Upload QR"])

with tab_url:
    url_input = st.text_input("Enter a URL:", placeholder="https://example.com")
    if st.button("Scan URL", type="primary"):
        if not url_input.strip():
            st.error("❌ Please enter a URL.")
        else:
            status, threats = classify_url(url_input)
            st.divider()
            st.markdown(f"**Scanned URL:** `{url_input}`")
            if status == "INVALID":
                st.error("❌ Invalid URL format.")
            elif status == "UNSAFE":
                st.error("🚨 Phishing Detected")
                st.write("Threat type(s):", ", ".join(threats))
            else:
                st.success("✅ Safe")

with tab_qr:
    uploaded = st.file_uploader(
        "Upload PNG or JPG QR code", type=["png", "jpg", "jpeg"]
    )
    if uploaded:
        url_from_qr = extract_url_from_qr(uploaded.read())
        if url_from_qr:
            status, threats = classify_url(url_from_qr)
            st.divider()
            st.markdown(f"**Decoded URL:** `{url_from_qr}`")
            if status == "UNSAFE":
                st.error("🚨 Phishing Detected")
                st.write("Threat type(s):", ", ".join(threats))
            else:
                st.success("✅ Safe")
        else:
            st.error("❌ Could not decode a valid URL from the image.")
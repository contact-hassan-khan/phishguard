# 🛡️ PhishGuard – URL & QR Phishing Detector

![license](https://img.shields.io/badge/license-MIT-green)
![demo](https://raw.githubusercontent.com/yourname/phishguard/main/demo.gif)

> **Detect phishing links instantly by pasting a URL or uploading a QR code.**  
> Powered by **Google Safe Browsing API v4**.

---

## ✨ Features

- 🔗 **Check URLs** for phishing, malware, and unwanted software
- 📷 **Scan QR codes** to extract and check embedded links
- ⚡ **Instant results** with a simple, modern UI
- 🔒 **No API keys stored** in code—safe for open source

---

## 🔑 1-Minute API-Key Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. **APIs & Services → Library** → search for **“Safe Browsing API”** → **Enable**.
3. **APIs & Services → Credentials → Create Credentials → API key**.
4. _(Recommended)_ **Restrict** the key to the **Safe Browsing API** only.

---

## 🚀 Run Locally

### 1. Clone & Install

```bash
git clone https://github.com/yourname/phishguard.git
cd phishguard
pip install -r requirements.txt
```

### 2. Set Your API Key

- **Recommended:** Create a `.env` file in the project root:
  ```
  GSB_API_KEY=YOUR_GOOGLE_KEY_HERE
  ```
- Or set it in your terminal:
  - **Linux/macOS:** `export GSB_API_KEY=YOUR_GOOGLE_KEY_HERE`
  - **Windows CMD:** `set GSB_API_KEY=YOUR_GOOGLE_KEY_HERE`
  - **Windows PowerShell:** `$env:GSB_API_KEY="YOUR_GOOGLE_KEY_HERE"`

### 3. Start the App

```bash
streamlit run app.py
```

---

## 🐳 Docker

Build and run with Docker:

```bash
docker build -t phishguard .
docker run -e GSB_API_KEY=YOUR_GOOGLE_KEY_HERE -p 8501:8501 phishguard
```

---

## 📦 Requirements

- Python 3.8+
- streamlit
- validators
- requests
- pyzbar
- pillow

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2025 yourname

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgements

- [Google Safe Browsing API](https://developers.google.com/safe-browsing/)
- [Streamlit](https://streamlit.io/)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)
- [Pillow](https://python-pillow.org/)

---

> **Security Tip:**  
> Never share your API key publicly or commit it to version control.
# PhishNet

**PhishNet** is a cybersecurity assistant that helps users detect phishing, scam, or suspicious emails using AI. It runs a lightweight model on mobile or wearable devices for privacy and speed, while delegating tough decisions to a cloud-based LLM. Designed especially for users in **Australia** and the **USA**, it incorporates local patterns, databases, and habits.

## Features

### 🔍 Local Detection
- Compact transformer model for offline scanning (TinyLlama or DistilBERT).
- Flags phishing, scams, and impersonation attempts quickly on-device.

### ☁️ Cloud Escalation
- For complex or uncertain emails, the app calls a large cloud-hosted LLM for a second opinion.

### 🧠 Email Context Enrichment
- Region-specific language models detect scams tied to:
  - Tax seasons (ATO, IRS)
  - Emergency relief scams
  - Election & health misinformation
- Adds context to known scam campaigns (Amazon, USPS, AusPost, etc.)

### 🔐 Personal Security Layer
- Verifies business identity:
  - Cross-check emails with Australian Business Numbers (ABN)
  - Detect fake businesses in the U.S. via BBB/WHOIS checks

### 📊 Behavioral Profiling
- Understands user patterns and raises alerts for:
  - Unfamiliar senders or irrelevant brands
  - Deviations from user email behavior

### 🌐 Dark Web Exposure Check
- Alerts users if their credentials or email are found in breach databases like HaveIBeenPwned.

### 📈 Analytics Dashboard
- Real-time dashboard to track:
  - Scam trends by region
  - Detection accuracy
  - False positive/negative rates
  - Escalation patterns

## Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/hemangsharma/phishnet.git
cd phishnet-ai
```

### 2. Set up the virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Train the local model:
```bash
cd edge-model/training
python train.py --data ../../data/emails.csv
```

### 4. Start the cloud API:
```bash
cd cloud-api
uvicorn app.main:app --reload
```
### 5. Launch the analytics dashboard:
```bash
cd analytics
streamlit run dashboard.py
```
## Contributing
We welcome developers, cybersecurity researchers, and hobbyists! Please open an issue or submit a PR with your enhancements.
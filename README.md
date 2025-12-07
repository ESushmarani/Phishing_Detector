# Phishing URL Detector 🔎🐍

A simple Python tool that checks if a URL is suspicious or phishing using rule‑based analysis.
Perfect mini‑project for cybersecurity beginners and interviews!

# Features

Detects phishing using 5 rule checks

Shows danger level, accuracy estimate, and triggered rules

Works completely offline

Lightweight & beginner‑friendly

# What It Checks
- Rule	Description
- @ Symbol	Common trick to mislead users
- Long URLs	Phishing URLs are usually very long
- IP Address in URL	Attackers hide behind numeric URLs
- Too Many Dots	Suspicious redirect patterns
- Hyphens -	Often used in fake domains

🧪 Example Output
Enter URL: http://123.55.22.11-login-secure-update.com

⚠️ Result: High Risk — Phishing URL Detected  
🚨 Danger Level: 80%  
🎯 Accuracy Estimate: 78%  
📌 Triggered Rules: 4/5  

# How to Run
1. Clone the project
git clone https://github.com/YOUR-USERNAME/phishing-url-detector

2. Run the script
python3 phishing_detector.py

# 📁 Project Structure
 📦 phishing-url-detector 
 
 ┣ 📜 phishing_detector.py
 
  ┗ 📜 README.md

## 🤝 Contributing

Feel free to fork this repo and improve the UI or add new features!

---

## 📜 License

This project is **free to use** for learning and personal purposes.

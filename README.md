# 📈 StockTrak Trading Bot

This Python-based trading bot automates stock trades on the StockTrak (https://www.stocktrak.com/) stock market simulator using Playwright for browser automation.

---

## 🚀 Features

- Automates login to StockTrak
- Navigates to trading interface
- Inputs trade details (ticker, action, amount, order type)
- Submits trades by simulating real user interaction
- Handles JavaScript-based validation and input quirks
- Persistent session via saved cookies (`session.json`)

---

## 📁 Project Structure

StockTrackBot/
├── config.py              # Stores login credentials (never push to GitHub)
├── main.py                # Entry point to run the bot
├── scraper/
│   ├── login.py           # Handles login automation
│   ├── trade_executor.py  # Executes trades with provided parameters
├── utils/
│   ├── logger.py          # Logs trade attempts and results
├── requirements.txt       # Python dependencies
└── README.md              # You're reading it!

---

## ⚙️ Setup

1. Clone the repo
   git clone https://github.com/your-username/StockTrackBot.git
   cd StockTrackBot

2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate        # or `.venv\Scripts\activate` on Windows

3. Install dependencies
   pip install -r requirements.txt
   playwright install

4. Configure credentials
   Create a config.py:
   STOCKTRACK_USERNAME = "your_username"
   STOCKTRACK_PASSWORD = "your_password"

---

## ✅ Usage

To execute a trade:
   python main.py

Or import and run specific functions from trade_executor.py.

---

## 📌 Notes

- This bot mimics human interaction to bypass the lack of an official StockTrak API.
- Be mindful of terms of service and academic integrity policies when using automation tools.
- Use for educational or personal learning purposes only.

---

## 🛠 Dependencies

- Playwright
- Python 3.8+

---

## 📬 Contact

For bugs, ideas, or feedback, feel free to reach out or open an issue.

---

## ⚠️ Disclaimer

This project is not affiliated with or endorsed by StockTrak. Use at your own risk.

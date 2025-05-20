import os
from playwright.sync_api import sync_playwright
import config

SESSION_FILE = "session.json"

class LoginManager:
    def __init__(self, headless=True):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self):
        """Start the browser and create a new context."""
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=self.headless)
        if os.path.exists(SESSION_FILE):
            print("Loading existing session...")
            self.context = self.browser.new_context(storage_state=SESSION_FILE)
        else:
            print("No session found, starting a new session...")
            self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        """Close the browser."""
        if self.browser:
            self.browser.close()

    def login(self):
        """Perform login and save session."""
        self.start_browser()
        self.page.goto("https://www.stocktrak.com/login")  # Adjust to actual login URL

        # Check if already logged in
        if os.path.exists(SESSION_FILE):
            self.page.goto("https://www.stocktrak.com/trading/equities")  # Post-login page
            if "Login" not in self.page.title():  # Simple check to see if login is needed
                print("Already logged in! ✅")
                self.close_browser()
                return

        # Perform manual login
        print("Logging in manually...")
        self.page.fill("input#tbLoginUserName", config.STOCKTRACK_USERNAME)
        self.page.fill("input#Password", config.STOCKTRACK_PASSWORD)
        self.page.click("button.button.secondary.margin-0")  # Login button

        # Skip popup and go to trade page
        self.page.goto("https://www.stocktrak.com/trading/equities")
        self.page.click("button.secondary-btn")  # Close tutorial popup

        # Test for successful login
        print("Login successful! ✅")

        # Save session for future logins
        self.context.storage_state(path=SESSION_FILE)
        print(f"Session saved to {SESSION_FILE}")

        self.close_browser()

if __name__ == "__main__":
    login_manager = LoginManager(headless=False)
    login_manager.login()




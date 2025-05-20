from playwright.sync_api import sync_playwright
import time

class Tradingbot:
    """
    A bot for automating trades on the StockTrak platform using Playwright.
    """

    def __init__(self, headless=True):
        """
        Initialize the Tradingbot instance.

        Args:
            headless (bool): Whether to run the browser in headless mode. Defaults to True.
        """
        self.headless = headless
        self.browser = None
        self.page = None
    
    def start_browser(self):
        """
        Start the Playwright browser and initialize the page context.
        """
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        context = self.browser.new_context(storage_state="session.json")
        self.page = context.new_page()

    def close_browser(self):
        """
        Close the browser if it is running.
        """
        if self.browser:
            self.browser.close()

    def go_to_equity_page(self):
        """
        Navigate to the equities trading page on StockTrak.
        """
        self.page.goto("https://www.stocktrak.com/trading/equities")
        print("Navigated to Equity page")
    
    def go_to_crypto_page(self):
        """
        Navigate to the cryptocurrency trading page on StockTrak.
        """
        self.page.goto("https://www.stocktrak.com/trading/crypto")
        print("Navigated to Crypto page")

    def select_symbol(self, symbol):
        """
        Select the trading symbol for the desired asset.

        Args:
            symbol (str): The trading symbol (e.g., stock ticker or crypto symbol).
        """
        self.page.fill("#tbSymbol", symbol)  # Update with correct selector
        self.page.click("body")
        print("Symbol Selected!")
    
    def select_action(self, action):
        """
        Select the trading action (e.g., Buy, Sell, Short, Cover).

        Args:
            action (str): The action to perform. Must be one of "Buy", "Sell", "Short", or "Cover".
        """
        actions = {
            "Buy": None,
            "Sell": "#sell-order",
            "Short": "#short-order",
            "Cover": "#cover-order" 
        }
        if action in actions:
            if actions[action]:
                self.page.click(actions[action])
            print("Action Selected")
        else:
            print("Invalid Action")
        
    def select_quantity(self, num_shares):
        """
        Specify the quantity of shares or units to trade.

        Args:
            num_shares (int): The number of shares or units to trade.
        """
        quantity_input = self.page.locator("#tbQuantity")
        quantity_input.fill("")
        quantity_input.type(str(num_shares))
        quantity_input.press("Enter")
        self.page.click("body")
        print("Quantity of Shares Selected")

    def select_order_type(self, order_type):
        """
        Select the type of order to place (e.g., Market, Limit, Stop).

        Args:
            order_type (str): The type of order. Must be one of "Market", "Limit", or "Stop".
        """
        order_types = {
            "Market": None,  # Default order type
            "Limit": "input[type='radio'][value='limit']",
            "Stop": "input[type='radio'][value='stop']"
        }
        if order_type in order_types:
            if order_types[order_type]:
                self.page.click(order_types[order_type])
            print(f"Order type '{order_type}' selected.")
        else:
            print("Order Type Invalid")

    def review_order(self):
        """
        Review the order by clicking the 'Preview Order' button.
        """
        self.page.wait_for_selector("#btnPreviewOrder", timeout=5000)
        self.page.click("#btnPreviewOrder")
        print("Order reviewed.")

    def confirm_order(self):
        """
        Confirm the order by clicking the 'Place Order' button.
        """
        self.page.wait_for_selector("#btnPlaceOrder", timeout=5000)  # Wait for Place Order button
        self.page.click("#btnPlaceOrder")  # Adjust selector if needed
        print("Order placed.")

    def execute_trade(self, symbol, action, num_shares, order_type):
        """
        Execute a trade by automating the entire process.

        Args:
            symbol (str): The trading symbol (e.g., stock ticker or crypto symbol).
            action (str): The action to perform (e.g., "Buy", "Sell", "Short", "Cover").
            num_shares (int): The number of shares or units to trade.
            order_type (str): The type of order (e.g., "Market", "Limit", "Stop").
        """
        try:
            self.start_browser()
            self.go_to_trade_page()
            self.select_symbol(symbol)
            self.select_action(action)
            self.select_quantity(num_shares)
            self.select_order_type(order_type)
            self.review_order()
            self.confirm_order()
            print("Trade executed successfully.")
        finally:
            self.close_browser()
from playwright.sync_api import Page
import os

def capture_screenshot(page: Page, name="screenshot"):
    """Takes a screenshot and saves it in the screenshots folder."""
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    path = f"screenshots/{name}.png"
    page.screenshot(path=path)
    print(f"Screenshot saved at: {path}")

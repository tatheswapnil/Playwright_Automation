import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/v1/")
        yield page  # Keeps the page open for all tests
        page.close()
        context.close()
        browser.close()

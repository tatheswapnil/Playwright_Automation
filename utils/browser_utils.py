from playwright.sync_api import sync_playwright

def launch_browser(headless=True, mobile=False):
    """Launch a new browser instance with configurable options."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        
        if mobile:
            context = browser.new_context(
                viewport={"width": 375, "height": 812},
                is_mobile=True
            )

        page = context.new_page()
        return browser, context, page

def close_browser(browser):
    """Closes the browser instance."""
    browser.close()

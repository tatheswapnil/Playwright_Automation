from playwright.sync_api import Page, TimeoutError

def wait_and_click(page: Page, selector: str, timeout=5000):
    """Waits for an element to be visible and then clicks it."""
    try:
        page.wait_for_selector(selector, timeout=timeout)
        page.click(selector)
    except TimeoutError:
        print(f"Element {selector} not found within {timeout}ms")

def wait_and_type(page: Page, selector: str, text: str, timeout=5000):
    """Waits for an element and types the given text into it."""
    try:
        page.wait_for_selector(selector, timeout=timeout)
        page.fill(selector, text)
    except TimeoutError:
        print(f"Unable to find {selector} to type text.")

def get_text(page: Page, selector: str):
    """Retrieves the text from a given element."""
    return page.inner_text(selector)

from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, locator, timeout=10000):
        """Waits until the element is visible before proceeding."""
        print(f"Waiting for element: {locator}")  # Debugging step
        try:
            expect(self.page.locator(locator)).to_be_visible(timeout=timeout)
            print(f"Element found: {locator}")
        except AssertionError:
            print(f"Element NOT found: {locator}")
            self.page.screenshot(path=f"screenshots/error_{locator.replace('/', '_')}.png")  # Take a screenshot
            raise

    def click_element(self, locator):
        """Click an element on the page."""
        self.wait_for_element(locator)
        self.page.locator(locator).click()

    def fill_text(self, locator, text):
        """Fill text in an input field."""
        self.wait_for_element(locator)
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        """Get text from an element."""
        self.wait_for_element(locator)
        return self.page.locator(locator).inner_text()

    def select_dropdown_option(self, locator, value):
        """Select a dropdown option by value."""
        self.wait_for_element(locator)
        self.page.locator(locator).select_option(value)

    def is_element_visible(self, locator):
        """Check if an element is visible."""
        return self.page.locator(locator).is_visible()

    def get_element_count(self, locator):
        """Get the count of elements matching the locator."""
        return self.page.locator(locator).count()

    def wait_for_navigation(self, url_substring, timeout=10000):
        """Wait for navigation to a specific URL."""
        self.page.wait_for_url(f"**{url_substring}**", timeout=timeout)

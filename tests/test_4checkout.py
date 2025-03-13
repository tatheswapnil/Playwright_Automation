from pages.checkout_page import CheckoutPage  

from utils.element_utils import wait_and_type
from utils.logger_utils import logger


from utils.element_utils import wait_and_click

from utils.screenshot_utils import capture_screenshot

def test_checkout(setup_browser):
    logger.info("Started: test_checkout")
    page = setup_browser
    checkout_page = CheckoutPage(page)

    assert "cart.html" in page.url, f"Unexpected URL: {page.url}"

   
    wait_and_click(page, "#checkout")

    # Fill in checkout details
    wait_and_type(page, "#first-name", "Swapnil")
    wait_and_type(page, "#last-name", "Patil")
    wait_and_type(page, "#postal-code", "12345")
    wait_and_click(page, "#continue")

    # Capture Screenshot at Review Page
    capture_screenshot(page, "checkout_review")

    # Click Finish
    wait_and_click(page, "#finish")

    # Capture Final Screenshot
    capture_screenshot(page, "checkout_complete")
    logger.info("Completed: test_checkout")

from utils.logger_utils import logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login(setup_browser):
    logger.info("Started: test_login")  # Ensure only one start log per test

    page = setup_browser
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.wait_for_inventory_page()

    logger.info("Completed: test_login")  
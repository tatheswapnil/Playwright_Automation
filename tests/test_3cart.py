from utils.logger_utils import logger
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(setup_browser):
    logger.info("Started: test_cart")
    page = setup_browser
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    inventory_page.wait_for_inventory_page()
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.verify_item_in_cart()
    logger.info("Completed: test_cart")

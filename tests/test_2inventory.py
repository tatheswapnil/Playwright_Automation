from utils.logger_utils import logger
from pages.inventory_page import InventoryPage

def test_inventory_sort(setup_browser):
    logger.info("Started: test_inventory")
    page = setup_browser
    inventory_page = InventoryPage(page)
    inventory_page.wait_for_inventory_page()
    inventory_page.sort_items("lohi")
    logger.info("Completed: test_inventory")

from pages.base_page import BasePage 

class InventoryPage(BasePage):
    INVENTORY_LIST = "//div[@class='inventory_list']"
    FIRST_ITEM_ADD_BUTTON = "(//button[contains(@class, 'btn_inventory')])[1]"
    SORT_DROPDOWN = "//select[@class='product_sort_container']"
    CART_BUTTON = "//a[@class='shopping_cart_link']"

    def wait_for_inventory_page(self):
        """Wait for inventory list to be visible"""
        self.wait_for_element(self.INVENTORY_LIST)

    def add_first_item_to_cart(self):
        """Add the first item to the cart"""
        self.click_element(self.FIRST_ITEM_ADD_BUTTON)

    def sort_items(self, sort_option):
        """Sort inventory items (Options: 'az', 'za', 'lohi', 'hilo')"""
        self.select_dropdown_option(self.SORT_DROPDOWN, sort_option)

    def go_to_cart(self):
        """Navigates to the cart page."""
        print(f"Current URL: {self.page.url}")  # Debugging
        self.page.wait_for_load_state("networkidle")
        
        # Check if element exists before clicking
        cart_locator = self.page.locator("//a[contains(@class, 'shopping_cart_link')]")
        
        if not cart_locator.is_visible():
            print("Cart button is NOT visible, taking screenshot...")
            self.page.screenshot(path="screenshots/cart_not_found.png")
            raise AssertionError("Cart button not found on the page.")
        
        cart_locator.click()
        print(f"URL after clicking cart: {self.page.url}")


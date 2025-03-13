from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = "//div[@class='cart_item']"
    CHECKOUT_BUTTON = "//button[@id='checkout']"

    def verify_item_in_cart(self):
        """Checks if an item is in the cart"""
        self.wait_for_element(self.CART_ITEM)

    def proceed_to_checkout(self):
        """Proceeds to checkout"""
        self.click_element(self.CHECKOUT_BUTTON)

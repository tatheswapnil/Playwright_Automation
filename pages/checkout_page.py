class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def enter_checkout_details(self, first_name, last_name, postal_code):
        """Enter checkout details and proceed."""
        print(f"Current URL before checkout: {self.page.url}")  # Debugging

        # Wait for checkout page to load
        self.page.wait_for_load_state("networkidle")

        if "checkout" not in self.page.url:
            print("Checkout page is NOT loaded, taking screenshot...")
            self.page.screenshot(path="screenshots/checkout_not_found.png")
            raise AssertionError("Checkout page did not load correctly.")

        # Enter details
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)

        # Click continue
        self.page.click("#continue")

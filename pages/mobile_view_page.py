from pages.base_page import BasePage

class MobileViewPage(BasePage):
    def test_mobile_view(self):
        """Tests the site on a mobile viewport"""
        mobile_context = self.page.context.browser.new_context(
            viewport={"width": 375, "height": 812},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
        )
        mobile_page = mobile_context.new_page()
        mobile_page.goto("https://www.saucedemo.com")
        mobile_page.screenshot(path="screenshots/mobile_view.png")

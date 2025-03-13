from pages.mobile_view_page import MobileViewPage
from utils.logger_utils import logger

def test_mobile_view(setup_browser):
    logger.info("Started: test_mobile_view")
    page = setup_browser
    mobile_view = MobileViewPage(page)
    mobile_view.test_mobile_view()
    logger.info("Completed: test_mobile_view\n")

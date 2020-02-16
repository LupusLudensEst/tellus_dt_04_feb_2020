from pages.main_page import MainPage
from pages.contact_us_page import ContactUsPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.contact_us_page = ContactUsPage(self.driver)
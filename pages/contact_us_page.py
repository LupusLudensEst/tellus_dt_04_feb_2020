from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class ContactUsPage(Page):

    # locators
    CONTACT_US_BTN = (By.CSS_SELECTOR, "a.n2-style-79bbf776d3d40577778e4b108270ea28-heading.n2-ow")
    FIRST_NAME = (By.ID, 'c-0-6')
    LAST_NAME = (By.ID, 'c-1-5')
    E_MAIL = (By.ID, 'c-2-4')
    PHONE = (By.ID, 'c-3-3')
    MESSAGE = (By.ID, 'c-4-2')
    SUBMIT_BTN = (By.ID, 'c-submit-button')
    TEXT = (By.CSS_SELECTOR, "div.c-forms-confirmation-message.c-html")

    def clck_contct_us_button(self):
        """
        Click on contact us button
        """
        self.click(*self.CONTACT_US_BTN)

    def frst_nm_entered(self, text):
        """
        Input first name in the iframe
        """
        sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            "//iframe[@src='https://services.cognitoforms.com/f/FFbINltml0S-xBx3VsN1lg?id=1']"))
        self.input_text(text, *self.FIRST_NAME)

    def lst_nm_entered(self, text):
        """
        Input last name
        """
        self.input_text(text, *self.LAST_NAME)

    def e_mail_entered(self, text):
        """
        Input e-mail
        """
        self.input_text(text, *self.E_MAIL)

    def phone_entered(self, text):
        """
        Input phone
        """
        self.input_text(text, *self.PHONE)

    def message(self, text):
        """
        Input message
        """
        self.input_text(text, *self.MESSAGE)

    def clck_sbmt_button(self):
        """
        Click on submit us button
        """
        self.click(*self.SUBMIT_BTN)
    sleep(4)

    def txt_is_here(self, text):
        """
        Text is here
        """
        self.verify_text(text, *self.TEXT)


from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    LOGN_BTN = (By.CSS_SELECTOR, "a.oauthloginbutton.btn.btn-social.btn-primary.da11y-submenu")
    LGN_FLD = (By.CSS_SELECTOR, "input#username.validate")
    PSWRD_FLD = (By.ID, "password")
    LOGN_BTN_ENTRD = (By.ID, "kc-login")
    ALRT_TEXT = (By.CSS_SELECTOR, "span.kc-feedback-text")

    def click_login_button(self):
        """
        Click on login button
        """
        self.click(*self.LOGN_BTN)

    def wrong_login(self, text):
        """
        Input wrong email into login
        """
        self.input_text(text, *self.LGN_FLD)

    def wrong_password(self, text):
        """
        Input wrong password
        """
        self.input_text(text, *self.PSWRD_FLD)

    def click_login_button_aftr_entrd(self):
        """
        Click on login button
        """
        self.click(*self.LOGN_BTN_ENTRD)
        sleep(4)

    def alert_is_here(self, text):
        """
        Alert is here
        """
        self.verify_text(text, *self.ALRT_TEXT)



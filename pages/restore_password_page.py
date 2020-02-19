from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class RestorePasswordPage(Page):

    # locators
    LGN_TLLS_BUTTON = (By.NAME, "oauthloginbutton btn btn-social btn-primary da11y-submenu")
    FORGOT_PASSWORD_BTN = (By.XPATH, "//a[@href='https://evv-dashboard.4tellus.net/forgot-password']") # (By.XPATH, "//a[@tabindex='5']")
    USER_NAME = (By.NAME, "userName")
    RESET_PASSWORD = (By.CSS_SELECTOR, "span.mat-button-wrapper")
    USR_NT_FND = (By.XPATH, "//span[@class='text']")

    def lgn_tlls_button(self):
        """
        click on Login Tellus EVV us button
        """
        self.click(*self.LGN_TLLS_BUTTON)

    def clck_frgt_pswd_button(self):
        """
        click forgot password button
        """
        self.click(*self.FORGOT_PASSWORD_BTN)

    def entr_usr_name(self, text):
        """
        enter user name
        """
        self.input_text(text, *self.USER_NAME)

    def clck_rst_pswd_button(self):
        """
        click on reset password button
        """
        self.click(*self.RESET_PASSWORD)
    sleep(8)

    def txt_s_here(self, text):
        """
        verify page has a text 'User not found'
        """
        self.verify_text(text, *self.USR_NT_FND)

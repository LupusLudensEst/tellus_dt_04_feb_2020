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

    def alert_is_here(self):
        """
        Alert is here
        """
        assert "Invalid user name or password." in self.driver.find_element(*self.ALRT_TEXT).text
        print('\nSign is here: ','"' ,str(self.driver.find_element(*self.ALRT_TEXT).text),'"' ,'.')



    # def click_on_forgot_password(self):
    #     """
    #     Clicks "Forgot Password?" button
    #     """
    #     self.click(*self.FORGOT_PASSWORD_BTN)
    #
    # def forgot_passw_instruct(self):
    #     """
    #     Verify "Enter your Email and we'll send you a link to change your password." sign is here
    #     """
    #     assert "Enter your Email and we'll send you a link to change your password" in self.driver.find_element(*self.FORGOT_PASSWORD_INSTR).text
    #     print('\nSign is here: ','"' ,str(self.driver.find_element(*self.FORGOT_PASSWORD_INSTR).text),'"' ,'.')
    #
    # def enter_email_for_restoring(self, text):
    #     """
    #     Input email "RestoreAccess@gmail.com" for restoring access
    #     """
    #     self.input_text(text, *self.FORGOT_EMAIL_FIELD)
    #
    # def click_on_restore_psswrd_btn(self):
    #     """
    #     Click on Request Password button
    #     """
    #     self.driver.find_elements(*self.RQST_PSWRD_BTN)[-1].click()
    #
    # def password_cnfrmtn_snt(self):
    #     """
    #     Verify "Password confirmation sent to RestoreAccess@gmail.com.Make sure you check your spam box." sign is here
    #     """
    #     assert "Password confirmation sent to RestoreAccess@gmail.com. Make sure you check your spam box." in self.driver.find_element(
    #         *self.PSSWRD_CNFRMTN_SNT).text
    #     print('\nSign is here: ', '"', str(self.driver.find_element(*self.PSSWRD_CNFRMTN_SNT).text), '"', '.')

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
LOGN_BTN = (By.CSS_SELECTOR, "a.oauthloginbutton.btn.btn-social.btn-primary.da11y-submenu")
FORGOT_PASSWORD_BTN = (By.XPATH, "//a[@tabindex='5']")
USER_NAME = (By.NAME, "userName")
RESET_PASSWORD = (By.CSS_SELECTOR, "span.mat-button-wrapper")
USR_NT_FND = (By.XPATH, "//span[@class='text']")


# open the url
driver.get( 'https://4tellus.com/' )
driver.implicitly_wait(10)

# click on login button
driver.find_element( *LOGN_BTN ).click()

# click forgot password button
driver.find_element( *FORGOT_PASSWORD_BTN ).click()

# enter user name
e = driver.find_element( *USER_NAME )
e.clear()
e.send_keys('LupusLudens')
sleep(4)

# click on reset password button
driver.find_element( *RESET_PASSWORD ).click()
sleep(4)

# verify page has a text 'User not found'
actual_text = driver.find_element( *USR_NT_FND ).text
assert 'User not found' in actual_text
print(f'Text is here: {actual_text} ')

# driver quit
driver.quit()

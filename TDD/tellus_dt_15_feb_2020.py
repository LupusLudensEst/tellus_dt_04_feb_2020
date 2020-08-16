from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
#CONTACT_US_BTN = (By.XPATH, "//a[@href='https://4tellus.com/contact-us/']")
#CONTACT_US_BTN = (By.CSS_SELECTOR, "li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-25718")
#CONTACT_US_BTN = ('https://4tellus.com/contact-us/')
#CONTACT_US_BTN = (By.PARTIAL_LINK_TEXT, 'https://4tellus.com/contact-us/')
CONTACT_US_BTN = (By.CSS_SELECTOR, "a.n2-style-79bbf776d3d40577778e4b108270ea28-heading.n2-ow") #(By. XPATH, "//li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-25718']")
FIRST_NAME =   (By.ID, 'c-0-6') #(By.XPATH, "(//div[@class='c-editor'])[2]") #(By.XPATH, "//*[@id='c-0-6']")#(By.XPATH, "//div[@data-field='FirstName']") #(By.XPATH, "//input[@id='c-0-6']") #(By.XPATH, "//input[@placeholder='First Name*']")  #(By.CSS_SELECTOR, "input#c-0-6")
LAST_NAME = (By.ID, 'c-1-5')
E_MAIL = (By.ID, 'c-2-4')
PHONE = (By.ID, 'c-3-3')
MESSAGE = (By.ID, 'c-4-2')
SUBMIT_BTN = (By.ID, 'c-submit-button')
TEXT = (By.CSS_SELECTOR, "div.c-forms-confirmation-message.c-html")

# open the url
driver.get( 'https://4tellus.com/' )
driver.implicitly_wait(10)

# Click on contact us button
driver.find_element( *CONTACT_US_BTN ).click()
sleep(2)

# open iframe
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@src='https://services.cognitoforms.com/f/FFbINltml0S-xBx3VsN1lg?id=1']"))

# Input first name
e = driver.find_element( *FIRST_NAME )
e.clear()
e.send_keys('Test_name')
sleep(2)

# Input last name
e = driver.find_element( *LAST_NAME )
e.clear()
e.send_keys('Test_last_name')
sleep(2)

# Input e-mail
e = driver.find_element( *E_MAIL )
e.clear()
e.send_keys('TestLogin1234!@gmail.com')
sleep(2)

# Input phone
e = driver.find_element( *PHONE )
e.clear()
e.send_keys('+1 407 435 44 33')
sleep(2)

# Input message
e = driver.find_element( *MESSAGE )
e.clear()
e.send_keys('Test_message')
sleep(2)

# Click on submit us button
driver.find_element( *SUBMIT_BTN ).click()

# verify page has a text 'Thank you! A representative will be in touch.'
actual_text = driver.find_element( *TEXT ).text
assert 'Thank you! A representative will be in touch.' in actual_text
print(f'Text is here: {actual_text} ')

# Return to default page, no need use here
# driver.switch_to.default_content()
# sleep(2)

# driver quit
driver.quit()
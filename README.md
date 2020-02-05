# tellus_dt_04_feb_2020
tellus_dt_04_feb_2020


Test Case

# Created by rapid at 2/04/2020
  Scenario: User enter wrong login and password and system rejects
    Given Loginpage
    Then Click on login button
    Then Wrong login "WrongLogin1234!@gmail.com"
    Then Wrong password "WrongPassword1234!"
    Then Click on login button after login and password are entered
    Then Verify "Invalid user name or password." sign is here
	
	Preconditions:
Runnable on: Windows 10
Browser: Chrome
Tools: Pycharm, Selenium Webdriver, Allure

Testcase steps:
1.	Go to https://4tellus.com/
2.	Click on login button
3.	Input wrong login "WrongPassword1234!@gmail.com".
4.	Input wrong password "WrongPassword1234!".
5.	Click on login button after login and password are entered.
6.	Verify "Invalid user name or password." text is here on the page.

Please put your code to GitHub.com and send the project link.

Thank you.

===========================================================================================
If you will install allure(java should be here)-you would be able to see the visual report. 
See steps:
$ pip install allure-behave
$ pip install allure-pytest
$ pip install pytest-allure-adaptor

to launch tests and generate reports folder: 
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
to extract report into browser: 
$ allure serve test_results/

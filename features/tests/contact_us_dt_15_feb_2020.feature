# Created by rapid at 2/15/2020
Feature: Contact us form

  Scenario: User enter info in the fields: 1. First Name, 2.Last Name, 3.Email Address, 4. Phone Number, 5. Message, etc.
    Given Loginpage
    Then Click on contact us button
    Then First Name Test_name
    Then Last Name Test_last_name
    Then Email Address TestLogin1234!@gmail.com
    Then Phone Number 1 407 435 44 33
    Then Message Test_message
    Then Click on Sumbit button
    Then Verify "Thank you! A representative will be in touch." sign is here
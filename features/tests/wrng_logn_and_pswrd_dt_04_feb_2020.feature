# Created by rapid at 2/4/2020
Feature: System rejects wrong login and password

  Scenario: User enter wrong login and password and system rejects
    Given Loginpage
    Then Wrong login "WrongLogin1234!@gmail.com"
    Then Wrong password "WrongPassword1234!"
    Then Click on login button
    Then Verify "Invalid user name or password." sign is here
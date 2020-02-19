# Created by rapid at 2/18/2020
Feature: Restore password

  Scenario: Restore password failed BC user is not registered
    Given Loginpage
    Then Click on login button
    Then Click on forgot password button
    Then Enter user name LupusLudens
    Then Click on reset password button
    Then Verify page has a text User not found
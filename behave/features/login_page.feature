Feature: Test login functionality of Gensom Solar

  Background:
    Given User should navigate to login page

  Scenario: Login with valid credentials
    When User enters "testuser100@testmail.com" email address
    And User enters "Password@1234" password
    And User clicks on Login button
    Then User should be redirected to overview dashboard page

  Scenario: Login with invalid credentials
    When User enters "testuser1001@testmail.com" unregistered email address
    And User enters "InvalidPassword" password
    And User clicks on Login button
    Then Error toaster message should be displayed

  Scenario: Login with blank email and password
    When User keeps email field and password field blank
    And User clicks on Login button
    Then Validation message should appear under email field and password field

  Scenario: User account is locked after five unsuccessful login attempts
    When User enters "testuser100@testmail.com" email address
    And User enters "InvalidPassword" incorrect password
    And User clicks on Login button 5 times
    Then First four toaster messages should display "Incorrect username or password"
    And Fifth toaster message should display "Your account has been temporarily blocked. Please try again after one hour."
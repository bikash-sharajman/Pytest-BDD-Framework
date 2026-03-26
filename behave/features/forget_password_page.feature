Feature: Forgot Password functionality

  Background:
    Given User should navigate to login page
    And User clicks on Forgot Password link
  @testing
  Scenario: Navigate to forgot password page
    Then User should be redirected to forgot password page

  Scenario: Generate OTP with valid details
    When User enters "testuser100@testmail.com" email address
    And User enters "+919861005263" phone number with country code
    And User clicks on Generate OTP button
    Then User should redirect to OTP verification page
    And success toaster message should be displayed

  Scenario: Generate OTP with blank email
    When User keeps the email field blank
    And User enters "+919861005263" phone number with country code
    And User clicks on Generate OTP button
    Then Toaster message should be displayed and prompt user to enter all required fields

  Scenario: Generate OTP with blank phone number
    When User enters "testuser100@testmail.com" email address
    And User keeps the phone number field blank
    And User clicks on Generate OTP button
    Then Toaster message should be displayed and prompt user to enter all required fields
Feature: OTP Verification and Update Password

  Background:
    Given User should navigate to login page
    And User clicks on Forgot Password link
    And User enters "testusergensom@gmail.com" email address
    And User enters "+918249973673" phone number with country code
    And User clicks on Generate OTP button
    And User should redirect to OTP verification page


  Scenario: Verify OTP successfully
    When User enters valid OTP in both email and phone number field
    And User clicks on Verify OTP button
    Then User should redirect to update password page
    And success toaster message should be displayed

  @testing
  Scenario: Verify invalid OTP
    When User enters invalid OTP in both email and phone number field
    And User try to verify with invalid otp 3 times
    Then First three toaster messages should display "Invalid OTP for Email. Please try again."
    And forth toaster message should display "Maximum validation attempts reached. Redirecting to login page."
    And User should redirect to login page to retry again

  Scenario: Update password successfully
    When User enters valid OTP in both email and phone number field
    And User clicks on Verify OTP button
    And User enters "Password@1234" in New Password field
    And User enters "Password@1234" in Confirm password field
    And User clicks on show password checkbox
    And User clicks on Update Password button
    Then Password should be updated successfully
    And User should be redirected to login page

  Scenario: Update password with mismatched passwords
    When User enters valid OTP in both email and phone number field
    And User clicks on Verify OTP button
    And User enters "Password@1234" in New Password field
    And User enters "Password@12345" valid incorrect password in Confirm password field
    And User clicks on Update Password button
    Then Password mismatch error toaster message should appear
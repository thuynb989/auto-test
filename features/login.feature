Feature: Login Amazon site

  @testcase01
  Scenario: Verify functionality of login with invalid account
    Given Navigate to the Amazon site
    And Home Page - User click "Sign in" button
    And Sign In Page - User input "aabbcc" into email field
    And Sign In Page - User tap "Continue" button
    Then Sign In Page - verify alert title is "There was a problem"
    Then Sign In Page - verify alert content is "We cannot find an account with that email address"
    And Sign In Page - User input "nguyenthibichthuy0801@gmail.com" into email field
    And Sign In Page - User tap "Continue" button
    And Sign In Page - User input "abc123" into "Password" field
    And Sign In Page - User click "Sign in" button
    Then Sign In Page - verify alert title is "There was a problem"
    Then Sign In Page - verify alert content is "Your password is incorrect"

  @testcase02
  Scenario: Verify functionality of login with valid account
    Given Navigate to the Amazon site
    And Home Page - User click "Sign in" button
    And Sign In Page - User input "nguyenthibichthuy0801@gmail.com" into email field
    And Sign In Page - User tap "Continue" button
    And Sign In Page - User input "P@ssw0rd" into "Password" field
    And Sign In Page - User click "Sign in" button
    Then Home Page - verify navigate account list is displayed with text "Hello, Thuy"



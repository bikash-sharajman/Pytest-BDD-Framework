Feature: Test the category module functionality

    Background:
        Given User is logged into the application
        And User navigates to Category module


    @regression @positive @testing
    Scenario: Add a new category
        When User click on add category button
        And User enter category name "Test category"
        And User click save button
        Then User should see category created success message


    @regression @positive @testing
    Scenario: View category details
        Given category "Test category" exists
        When User search for "Test category"
        And User click on view button
        Then User should see the category details page
        And the category name should be "Test category"


    @regression @positive @testing
    Scenario: Edit category
        Given category "Test category" exists
        When User search for "Test category"
        And User click on edit button
        And User clear and enter category name "Test category Updated"
        And User click update button
        Then User should see category updated success message


    @regression @positive @testing
    Scenario: Delete category
        Given category "Test category Updated" exists
        When User search for "Test category Updated"
        And User click on delete button
        And User confirm delete
        Then User should see "Category deleted successfully." success message



    @negative
    Scenario: Add duplicate category
        Given category "Test category" exists
        When User click on add category button
        And User enter category name "Test category"
        And User click save button
        Then Toaster message contains "already exists" should be displayed
    
    
    @negative
    Scenario: Add category without name
        When User click on add category button
        And User click save button
        Then Validation message "This field is required!" should be displayed



Feature: Sub Category Module Functionality

    Background:
        Given User is logged into the application
        And User navigates to sub category module

    # -------------------- CREATE --------------------

    @regression @positive @testing
    Scenario: Add a new sub category
        When User clicks on add subcategory button
        And User selects category "Demo category"
        And User enters name "Demo sub category"
        And User click save button
        Then User should see sub category created success message
        And "Demo sub category" should be visible in the list

    # -------------------- VIEW --------------------

    @regression @positive @testing
    Scenario: View sub category details
        Given sub category "Demo sub category" exists
        When User search for "Demo sub category"
        And User click on view button
        Then User should see the sub category details page
        # And the name should be "Demo sub category"

    # -------------------- UPDATE --------------------

    @regression @positive @testing
    Scenario: Edit sub category
        Given sub category "Demo sub category" exists
        When User search for "Demo sub category"
        And User click on edit button
        And User clear and enter name "Demo sub category updated"
        And User click update button
        Then User should see sub category updated success message
        And "Demo sub category updated" should be visible in the list

    # -------------------- DELETE --------------------

    @regression @positive @testing
    Scenario: Delete sub category
        # Given sub category "Demo sub category updated" exists
        When User search for "Demo sub category updated"
        And User click on delete button
        And User confirm delete
        Then User should see sub category deleted success message
        And "Demo sub category updated" should not be visible in the list

    # -------------------- NEGATIVE --------------------

    @negative
    Scenario: Add sub category without selecting category
        When User clicks on add subcategory button
        And User enters name "Demo sub category"
        And User click save button
        Then sub category Validation message "Category is required." should be displayed

    @negative
    Scenario: Add sub category without name
        When User clicks on add subcategory button
        And User selects category "Demo category"
        And User click save button
        Then sub category Validation message "Sub Category Name is required." should be displayed

    @negative
    Scenario: Add duplicate sub category
        Given sub category "Demo sub category" exists
        When User clicks on add subcategory button
        And User selects category "Demo category"
        And User enters name "Demo sub category"
        And User click save button
        Then sub category Toaster message contains "Sub Category already exists" should be displayed

Feature: Test the make module functionality

    Background:
        Given User is logged into the application
        And User navigates to make module

# -------------------- CREATE --------------------

    @regression @positive
    Scenario: Add a new make
        When User click on add make button
        And User enter make name "Test Make"
        And User click save button
        Then User should see make created success message
        And "Test Make" should be visible in the list

    # -------------------- VIEW --------------------

    @regression @positive 
    Scenario: View make details
        Given make "Test Make" exists
        When User search for "Test Make"
        And User click on view button
        Then User should see the make details page
        And the make name should be "Test Make"

    # -------------------- UPDATE --------------------

    @regression @positive 
    Scenario: Edit make
        Given make "Test Make" exists
        When User search for "Test Make"
        And User click on edit button
        And User clear and enter make name "Test Make Updated"
        And User click update button
        Then User should see make updated success message
        And "Test Make Updated" should be visible in the list

    # -------------------- DELETE --------------------

    @regression @positive @testing
    Scenario: Delete make
        Given make "Test Make Updated" exists
        When User search for "Test Make Updated"
        And User click on delete button
        And User confirm delete
        Then User should see make deleted success message
        And "Test Make Updated" should not be visible in the list

    @negative
    Scenario: Add duplicate make
        Given make "Test Make" exists
        When User click on add make button
        And User enter make name "Test Make"
        And User click save button
        Then Toaster message contains "already exists" should be displayed

    @negative
    Scenario: Add make without name
        When User click on add make button
        And User click save button
        Then Validation message "This field is required!" should be displayed

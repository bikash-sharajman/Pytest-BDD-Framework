Feature: Project Management - Basic Details Validation

    Background:
        Given User is logged into the application
        And Navigate to Project Management
        And Click on Add Project button

    @regression @positive @testing
    Scenario: Add project with all valid mandatory fields
        When User enters project code "Test Project"
        And User enters project name "Test Project"
        And User enters short name "TP"
        And User enters site address "Delhi"
        And User selects state "Delhi"
        And User enters latitude "20.2961"
        And User enters longitude "85.8245"
        And User selects cluster type "demo"
        And User selects billing entity "New test3"
        And User selects project type "Solar Management System"
        And User selects project sub type "Solar Power Storage"
        And User selects technology type "Monocrystalline"
        And User selects installation type "Rooftop"
        And User selects mounting type "Fixed Tilt"
        And User enters tilt azimuth "30"
        And User enters DC capacity "100"
        And User enters AC capacity "80"
        And User selects the commissioning date
        And User selects warehouse "Testing Warehouse"
        And User enters tariff "5"
        And User selects data frequency "5 Minutes"
        And User enters start time "06:00AM"
        And User enters end time "06:00PM"
        And User enters display order "1000"
        And User click save button
        Then User should see project created success message
        Then Project privilege provided to the user

    @negative
    Scenario: Submit form with all fields empty
        When User click save button 
        Then Validation message "This field is required!" should be displayed.

    @negative2
    Scenario: All tabs are disabled when basic details are not filled
        Then the following tabs should be disabled
            | tab_name             |
            | Unit Details         |
            | Data Logger details  |
            | Asset Details        |
            | Data Acquisition     |
            | Forecast Information |
            | Contact Details      |
            | Site Person Details  |
            | Vendor Details       |
            | Documents            |
            | Anomaly Detection    |


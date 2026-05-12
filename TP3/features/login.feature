@login
Feature: login
    As a user
    I want to login
    In order to buy sauce

    Scenario Outline: The user should login successfully
        Given the user is on the login page
        When the user log in with their <username> and their <password>
        Then the user is connected
            And the user is on the catalogue page

    Examples:
        | username      | password      |
        | standard_user | secret_sauce  |
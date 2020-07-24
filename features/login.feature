@login
Feature: Login
  As a user of my Demo App
  I want to Login
  So that I can interact with the app

  @happyPath
  Scenario: Valid Login
    Given I access my Demo App
    When I "demo" log in with password "mode"
    Then welcome page should display

  @negative
  Scenario Outline: Invalid Login
    Given I access my Demo App
    When I "<username>" log in with password "<password>"
    Then error page should display
    Examples:
      | username | password |
      | demo     | bad      |
      | bad      | mode     |
      |          | mode     |
      | bad      |          |

@login
Feature: Login
  As a user of my Demo App
  I want to Login
  So that I can interact with the app

  Background:
    Given I access my Demo App

  @happyPath
  Scenario: Valid Login
    When I log in with user "demo" and password "mode"
    Then welcome page should display

  @negative
  Scenario Outline: Invalid Login
    When I log in with user "<username>" and password "<password>"
    Then error page should display
    Examples:
      | username | password |
      | demo     | bad      |
      | bad      | mode     |
      |          | mode     |
      | bad      |          |

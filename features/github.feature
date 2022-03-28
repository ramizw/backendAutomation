# Created by Ramiz-Learn at 24-03-2022
Feature: GitHub API Validation
  # Enter feature description here

  Scenario: Session Management Check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then Status code of response should be 200

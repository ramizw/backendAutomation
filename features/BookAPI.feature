# Created by Ramiz-Learn at 19-03-2022
Feature: Verify if Books are added and deleted Using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API Functionality
    Given the Book details which needs to be added to Library
    When we execute AddBook post API method
    Then book is successfully added
    And Status code of response should be 200

#For parametrization with multiple data sets
#Test data here can be given by product owners
  @library
  Scenario Outline: Verify AddBook API Functionality 2
    Given the Book details with <isbn> and <aisle>
    When we execute AddBook post API method 2
    Then book is successfully added 2
    Examples:
      | isbn  |  aisle |
      | c2rd7  | 5881   |
      | c1q25t | 7414     |



# behave features/BookAPI.feature --no-capture --tags=smoke
#behave features/BookAPI.feature --no-capture --tags=<tagname>

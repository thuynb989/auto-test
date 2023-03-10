Feature: Search function

  @testcase03
  Scenario: Verify result list is paginated if there are more than 16 items
    Given Navigate to the Amazon site
    And Home Page - User click "All" dropdown
    And Home Page - User select department is "Books"
    And Home Page - User input value "apple" into "Search" field
    And Home Page - User click "Search" icon
    And Search Result Page - Scroll to "English" check box
    And Search Result Page - User check "English" check box
    Then Search Result Page - Verify search result is paginated
    Then Search Result Page - The number of items is "16" in each page

  @testcase04
  Scenario: Verify result list can be sorted on demand
    Given Navigate to the Amazon site
    And Home Page - User click "All" dropdown
    And Home Page - User select department is "Books"
    And Home Page - User input value "apple" into "Search" field
    And Home Page - User click "Search" icon
    And Search Result Page - Scroll to "English" check box
    And Search Result Page - User check "English" check box
    And Home Page - User click "Advanced Search" tab
    And Advanced Search Page - User click "Publication Date" dropdown
    And Advanced Search Page - User click "Search" button
    Then Search Result Page - Verify the result is sorted by Publication date





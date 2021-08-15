# Created by geotech at 13/08/2021
Feature: Verify Calculator Page functionalities

  Background: Open Calculator Page and Switch to iframe=fullframe
    Given I open Calculator Page
    When I switch to iframe=fullframe

  @regression @subtraction @division @addition @single-operator
  Scenario Outline: Verify Single Operator Subtraction, Division, Addition
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value2>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1 | operator      | value2 | expected_result |
      | 0      | Keys.SUBTRACT | a      | 0               |
      | 0      | Keys.ADD      |        | 0               |
      | 0      | Keys.SUBTRACT | 0      | 0               |
      | 0      | Keys.SUBTRACT | 5      | -5              |
      | 0      | Keys.SUBTRACT | -10    | -10             |
      |        | Keys.ADD      |        | 0               |
      |        | Keys.SUBTRACT | !      | 0               |
      |        | Keys.DIVIDE   | 0      | Error           |
      |        | Keys.DIVIDE   | 5      | 0               |
      | 4      | Keys.ADD      |        | 8               |
      | 4      | Keys.SUBTRACT |        | 0               |
      | 10     | Keys.DIVIDE   | 0      | Error           |
      | 50     | Keys.ADD      | 100    | 150             |
      | 6      | Keys.SUBTRACT | -9     | -3              |
      | -5     | Keys.ADD      |        | -10             |
      | -5     | Keys.SUBTRACT |        | 0               |
      | -5     | Keys.DIVIDE   |        | -1              |
      | -50    | Keys.SUBTRACT | -40    | -90             |

  @regression @subtraction @division @addition @multiple-operator
  Scenario Outline: Verify Single Operator Subtraction, Division, Addition
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<value2>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "<value4>"
    And I enter value into Calculator = "<value5>"
    And I enter value into Calculator = "<value6>"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1        | value2        | value3        | value4        | value5        | value6      | expected_result |
      | Keys.SUBTRACT | 5             | Keys.DIVIDE   | Keys.SUBTRACT | 5             | Keys.EQUALS | -10             |
      | 5             | Keys.SUBTRACT | Keys.SUBTRACT | 5             |               | Keys.EQUALS | 0               |
      | 5             | Keys.SUBTRACT | Keys.ADD      | 5             |               | Keys.EQUALS | 10              |
      | 30            | Keys.SUBTRACT | Keys.DIVIDE   | 10            |               | Keys.EQUALS | 3               |
      | 5             | Keys.ADD      | 8             | Keys.DIVIDE   | 4             | Keys.EQUALS | 7               |
      | 5             | Keys.SUBTRACT | 7             | Keys.DIVIDE   | 2             | Keys.EQUALS | 1.5             |
      | 5             | Keys.DIVIDE   | 5             | Keys.SUBTRACT | 6             | Keys.EQUALS | -5              |
      | Keys.ADD      | 5             | Keys.SUBTRACT | Keys.ADD      | 5             | Keys.EQUALS | 10              |
      | Keys.DIVIDE   | 5             | Keys.ADD      | Keys.SUBTRACT | 2             | Keys.EQUALS | -2              |
      | Keys.SUBTRACT | 5             | Keys.DIVIDE   | 2             | Keys.SUBTRACT | Keys.EQUALS | 0               |
      | Keys.ADD      | 5             | Keys.SUBTRACT | -6            | Keys.DIVIDE   | Keys.EQUALS | 4               |
      | Keys.DIVIDE   | 5             | Keys.ADD      | 6             | Keys.SUBTRACT | Keys.EQUALS | 0               |
      | Keys.SUBTRACT | 5             | Keys.EQUALS   | Keys.EQUALS   | Keys.EQUALS   |             | -15             |
      | Keys.ADD      | 5             | Keys.EQUALS   | Keys.EQUALS   | Keys.EQUALS   |             | 15              |
      | 50            | Keys.DIVIDE   | 5             | Keys.EQUALS   | Keys.EQUALS   |             | 2               |

  @regression @subtraction @division @addition @data-type
  Scenario Outline: Verify data type: Float Number, Percentage x Operator
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1 | operator      | value3 | expected_result |
      | 0.5    | Keys.ADD      | 1      | 1.5             |
      | 0.6    | Keys.SUBTRACT | 0.1    | 0.5             |
      | 0.1    | Keys.SUBTRACT | 0.6    | -0.5            |
      | 0.5    | Keys.DIVIDE   | 5      | 0.1             |
      | 0.5    | Keys.DIVIDE   | 0      | Error           |
      | 50%    | Keys.ADD      | 1      | 1.5             |
      | 60%    | Keys.SUBTRACT | 0.1    | 0.5             |
      | 10%    | Keys.SUBTRACT | 0.6    | -0.5            |
      | 50%    | Keys.DIVIDE   | 5      | 0.1             |
      | 50%    | Keys.DIVIDE   | 0      | Error           |

  @regression @subtraction @division @addition @boundary-value @ad-hoc
  Scenario Outline: Verify boundary value of Calculator
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1    | operator | value3 | expected_result |
      | 999999999 | Keys.ADD | 1      | 1e+9            |
      | 1234567   |          | 8      | 12345678        |
      | 12345678  |          | 9      | 123456789       |
      | 123456789 |          | 0      | 123456789       |

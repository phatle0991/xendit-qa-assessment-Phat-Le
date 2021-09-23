# Created by geotech at 23/09/2021
Feature: Account Callback
  Background:
    Given I login as a XenPlatform Entity Account
    And I enable XenPlatform

  @zenplatform @callback @account-callback
  Scenario Outline: Verify Owned Account Callback behavior
    Given I set Callback URL - Account created = <callback_url>
    And I set Auto-retry for failed callback is "<auto_retry_status>"
    When I create <account_type> Account by API <create_account_version>
    And Callback response time is <response_time>
    Then I verify Callback Request is <sent_callback>
    And I verify Callback Response Status is <callback_status>
    And I verify automatic retry is <auto_retry_trigger>
    Examples:
      | callback_url                                              | auto_retry_status | account_type   | create_account_version | response_time | sent_callback | callback_status      | auto_retry_trigger |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Enabled           | OWNED          | v1                     | any           | False         | N/A                  | False              |
      | http://fdjsfhasdf.com/                                    | Enabled           | OWNED          | v2                     | any           | True          | CALLBACK_URL_NOT_SET | False              |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Enabled           | OWNED          | v2                     | 30s           | True          | FAILED               | True               |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Disabled          | OWNED          | v2                     | 30s           | True          | FAILED               | False              |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Enabled           | OWNED          | v2                     | 29s           | True          | COMPLETED            | False              |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Enabled           | MANAGED        | v2                     | any           | False         | N/A                  | False              |
      | https://webhook.site/4bd3a861-dcbc-446c-988a-81c5eddc1a7d | Enabled           | Custom Acounts | v2                     | any           | False         | N/A                  | False              |
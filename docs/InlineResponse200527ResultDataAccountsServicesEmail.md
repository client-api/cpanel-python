# InlineResponse200527ResultDataAccountsServicesEmail

Information that indicates the Subaccount's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the Subaccount can access Webmail, POP, and IMAP services.  * &#x60;1&#x60; — Has service access. * &#x60;0&#x60; — Does **not** have service access. | [optional] 
**quota** | **int** | The Subaccount&#39;s email disk space quota, in megabytes (MB).  * &#x60;0&#x60; — The account has an unlimited email disk space quota. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts_services_email import InlineResponse200527ResultDataAccountsServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccountsServicesEmail from a JSON string
inline_response200527_result_data_accounts_services_email_instance = InlineResponse200527ResultDataAccountsServicesEmail.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccountsServicesEmail.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_services_email_dict = inline_response200527_result_data_accounts_services_email_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccountsServicesEmail from a dict
inline_response200527_result_data_accounts_services_email_from_dict = InlineResponse200527ResultDataAccountsServicesEmail.from_dict(inline_response200527_result_data_accounts_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



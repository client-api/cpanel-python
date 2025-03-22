# InlineResponse200529ResultDataServicesEmail

Information that indicates the account's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the account can access Webmail, POP, and IMAP services. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**quota** | **int** | The account&#39;s email disk space quota. * The set quota megabyte (MB) limit for the account&#39;s email disk space. * &#x60;0&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data_services_email import InlineResponse200529ResultDataServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultDataServicesEmail from a JSON string
inline_response200529_result_data_services_email_instance = InlineResponse200529ResultDataServicesEmail.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultDataServicesEmail.to_json())

# convert the object into a dict
inline_response200529_result_data_services_email_dict = inline_response200529_result_data_services_email_instance.to_dict()
# create an instance of InlineResponse200529ResultDataServicesEmail from a dict
inline_response200529_result_data_services_email_from_dict = InlineResponse200529ResultDataServicesEmail.from_dict(inline_response200529_result_data_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



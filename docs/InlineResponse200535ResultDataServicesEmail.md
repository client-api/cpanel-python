# InlineResponse200535ResultDataServicesEmail

This object contains the information that indicates the subaccount's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Webmail, POP, and IMAP services.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**quota** | **int** | The maximum amount of disk space allocated to subaccount&#39;s email account. A positive integer that represents the maximum disk space that the subaccount may use, in megabytes (MB).  **Note:**  This function will **not** return &#x60;0&#x60; as a value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200535_result_data_services_email import InlineResponse200535ResultDataServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200535ResultDataServicesEmail from a JSON string
inline_response200535_result_data_services_email_instance = InlineResponse200535ResultDataServicesEmail.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200535ResultDataServicesEmail.to_json())

# convert the object into a dict
inline_response200535_result_data_services_email_dict = inline_response200535_result_data_services_email_instance.to_dict()
# create an instance of InlineResponse200535ResultDataServicesEmail from a dict
inline_response200535_result_data_services_email_from_dict = InlineResponse200535ResultDataServicesEmail.from_dict(inline_response200535_result_data_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



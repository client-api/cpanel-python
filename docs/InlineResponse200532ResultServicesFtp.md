# InlineResponse200532ResultServicesFtp

An object containing the information that indicates the subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access FTP. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s FTP home directory relative to the cPanel account&#39;s home. | [optional] 
**quota** | **int** | The subaccount&#39;s FTP disk space quota. * &#x60;0&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200532_result_services_ftp import InlineResponse200532ResultServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200532ResultServicesFtp from a JSON string
inline_response200532_result_services_ftp_instance = InlineResponse200532ResultServicesFtp.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200532ResultServicesFtp.to_json())

# convert the object into a dict
inline_response200532_result_services_ftp_dict = inline_response200532_result_services_ftp_instance.to_dict()
# create an instance of InlineResponse200532ResultServicesFtp from a dict
inline_response200532_result_services_ftp_from_dict = InlineResponse200532ResultServicesFtp.from_dict(inline_response200532_result_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



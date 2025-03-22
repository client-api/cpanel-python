# InlineResponse200535ResultDataServicesFtp

This object contains the information that indicates the subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access FTP. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s FTP home directory. | [optional] 
**quota** | **int** | The subaccount&#39;s FTP disk space quota. * &gt;&#x3D; &#x60;1&#x60; - Represents the maximum disk space that the subaccount may use, in megabytes (MB). * &#x60;0&#x60;   - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200535_result_data_services_ftp import InlineResponse200535ResultDataServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200535ResultDataServicesFtp from a JSON string
inline_response200535_result_data_services_ftp_instance = InlineResponse200535ResultDataServicesFtp.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200535ResultDataServicesFtp.to_json())

# convert the object into a dict
inline_response200535_result_data_services_ftp_dict = inline_response200535_result_data_services_ftp_instance.to_dict()
# create an instance of InlineResponse200535ResultDataServicesFtp from a dict
inline_response200535_result_data_services_ftp_from_dict = InlineResponse200535ResultDataServicesFtp.from_dict(inline_response200535_result_data_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



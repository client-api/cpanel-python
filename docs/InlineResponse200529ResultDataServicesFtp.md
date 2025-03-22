# InlineResponse200529ResultDataServicesFtp

Information about the account's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the account can access FTP. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The account&#39;s FTP home directory. * A valid path, relative to the cPanel account&#39;s home directory. | [optional] 
**quota** | **int** | The account&#39;s FTP disk space quota. * An integer that represents the account&#39;s maximum FTP disk usage, in megabytes (MB). * &#x60;0&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data_services_ftp import InlineResponse200529ResultDataServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultDataServicesFtp from a JSON string
inline_response200529_result_data_services_ftp_instance = InlineResponse200529ResultDataServicesFtp.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultDataServicesFtp.to_json())

# convert the object into a dict
inline_response200529_result_data_services_ftp_dict = inline_response200529_result_data_services_ftp_instance.to_dict()
# create an instance of InlineResponse200529ResultDataServicesFtp from a dict
inline_response200529_result_data_services_ftp_from_dict = InlineResponse200529ResultDataServicesFtp.from_dict(inline_response200529_result_data_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



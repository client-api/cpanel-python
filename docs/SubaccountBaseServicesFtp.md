# SubaccountBaseServicesFtp

Information about the subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access FTP. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s FTP home directory, relative to the cPanel account&#39;s home directory. | [optional] 
**quota** | **str** | The subaccount&#39;s maximum FTP disk space quota, in megabytes (MB). * A string containing a non-negative float. * &#x60;0.00&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_base_services_ftp import SubaccountBaseServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBaseServicesFtp from a JSON string
subaccount_base_services_ftp_instance = SubaccountBaseServicesFtp.from_json(json)
# print the JSON string representation of the object
print(SubaccountBaseServicesFtp.to_json())

# convert the object into a dict
subaccount_base_services_ftp_dict = subaccount_base_services_ftp_instance.to_dict()
# create an instance of SubaccountBaseServicesFtp from a dict
subaccount_base_services_ftp_from_dict = SubaccountBaseServicesFtp.from_dict(subaccount_base_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



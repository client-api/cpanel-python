# ServiceAccountServicesFtp

This object contains the information that indicates the subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access FTP. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - Cannot access. | [optional] 
**homedir** | **str** | The subaccount&#39;s FTP home directory, relative to the cPanel account&#39;s home directory. | [optional] 
**quota** | **int** | The subaccount&#39;s FTP disk space quota. * &#x60;1&#x60; to &#x60;999999&#x60; - The maximum disk space that the subaccount may use, in megabytes (MB). * &#x60;0&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.service_account_services_ftp import ServiceAccountServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountServicesFtp from a JSON string
service_account_services_ftp_instance = ServiceAccountServicesFtp.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountServicesFtp.to_json())

# convert the object into a dict
service_account_services_ftp_dict = service_account_services_ftp_instance.to_dict()
# create an instance of ServiceAccountServicesFtp from a dict
service_account_services_ftp_from_dict = ServiceAccountServicesFtp.from_dict(service_account_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EditUserSubaccountBaseServicesFtp

This object contains the information that indicates the subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access FTP.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s FTP home directory. | [optional] 
**quota** | **int** | The maximum amount disk space, in megabytes (MB), that the subaccount may use.  * A positive integer between &#x60;1&#x60; and &#x60;999999&#x60; * &#x60;0&#x60; - Unlimited. | [optional] 

## Example

```python
from clientapi_cpanel.models.edit_user_subaccount_base_services_ftp import EditUserSubaccountBaseServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSubaccountBaseServicesFtp from a JSON string
edit_user_subaccount_base_services_ftp_instance = EditUserSubaccountBaseServicesFtp.from_json(json)
# print the JSON string representation of the object
print(EditUserSubaccountBaseServicesFtp.to_json())

# convert the object into a dict
edit_user_subaccount_base_services_ftp_dict = edit_user_subaccount_base_services_ftp_instance.to_dict()
# create an instance of EditUserSubaccountBaseServicesFtp from a dict
edit_user_subaccount_base_services_ftp_from_dict = EditUserSubaccountBaseServicesFtp.from_dict(edit_user_subaccount_base_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



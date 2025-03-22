# EditUserSubaccountBaseServicesEmail

This object contains the information that indicates the subaccount's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Webmail, POP, and IMAP services.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**quota** | **int** | The maximum amount of disk space, in megabytes (MB), allocated to the subaccount&#39;s email account.  **Note:**    This function will not return &#x60;0&#x60; as a value. | [optional] 

## Example

```python
from clientapi_cpanel.models.edit_user_subaccount_base_services_email import EditUserSubaccountBaseServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSubaccountBaseServicesEmail from a JSON string
edit_user_subaccount_base_services_email_instance = EditUserSubaccountBaseServicesEmail.from_json(json)
# print the JSON string representation of the object
print(EditUserSubaccountBaseServicesEmail.to_json())

# convert the object into a dict
edit_user_subaccount_base_services_email_dict = edit_user_subaccount_base_services_email_instance.to_dict()
# create an instance of EditUserSubaccountBaseServicesEmail from a dict
edit_user_subaccount_base_services_email_from_dict = EditUserSubaccountBaseServicesEmail.from_dict(edit_user_subaccount_base_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



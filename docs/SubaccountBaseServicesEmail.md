# SubaccountBaseServicesEmail

Information about the subaccount's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Webmail, POP, and IMAP services. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**quota** | **int** | The maximum amount of disk space, in megabytes (MB), allocated to subaccount&#39;s email account. | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_base_services_email import SubaccountBaseServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBaseServicesEmail from a JSON string
subaccount_base_services_email_instance = SubaccountBaseServicesEmail.from_json(json)
# print the JSON string representation of the object
print(SubaccountBaseServicesEmail.to_json())

# convert the object into a dict
subaccount_base_services_email_dict = subaccount_base_services_email_instance.to_dict()
# create an instance of SubaccountBaseServicesEmail from a dict
subaccount_base_services_email_from_dict = SubaccountBaseServicesEmail.from_dict(subaccount_base_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



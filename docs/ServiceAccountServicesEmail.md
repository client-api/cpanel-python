# ServiceAccountServicesEmail

Information that indicates the subaccount's email status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Webmail, POP, and IMAP services. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - Cannot access. | [optional] 
**quota** | **int** | The maximum amount of disk space allocated to subaccount&#39;s email account, in megabytes (MB). | [optional] 

## Example

```python
from clientapi_cpanel.models.service_account_services_email import ServiceAccountServicesEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountServicesEmail from a JSON string
service_account_services_email_instance = ServiceAccountServicesEmail.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountServicesEmail.to_json())

# convert the object into a dict
service_account_services_email_dict = service_account_services_email_instance.to_dict()
# create an instance of ServiceAccountServicesEmail from a dict
service_account_services_email_from_dict = ServiceAccountServicesEmail.from_dict(service_account_services_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



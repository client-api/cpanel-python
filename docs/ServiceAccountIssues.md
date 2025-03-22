# ServiceAccountIssues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | The affected section of cPanel &amp; WHM. | [optional] 
**limit** | **int** | The set quota megabyte (MB) limit for the affected subaccount. | [optional] 
**message** | **str** | The description of the issue. | [optional] 
**service** | **str** | The affected service. | [optional] 
**type** | **str** | The type of issue. | [optional] 
**used** | **int** | The number of megabytes (MB) that the account currently uses. | [optional] 

## Example

```python
from clientapi_cpanel.models.service_account_issues import ServiceAccountIssues

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountIssues from a JSON string
service_account_issues_instance = ServiceAccountIssues.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountIssues.to_json())

# convert the object into a dict
service_account_issues_dict = service_account_issues_instance.to_dict()
# create an instance of ServiceAccountIssues from a dict
service_account_issues_from_dict = ServiceAccountIssues.from_dict(service_account_issues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



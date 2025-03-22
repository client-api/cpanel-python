# EditUserSubaccountBaseIssues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | The affected section of cPanel &amp; WHM. | [optional] 
**limit** | **int** | The set quota megabyte (MB) limit for the affected subaccount. | [optional] 
**message** | **str** | The description of the issue. | [optional] 
**service** | **str** | The affected service. * &#x60;email&#x60; * &#x60;ftp&#x60; * &#x60;webdisk&#x60; | [optional] 
**type** | **str** | The type of issue. * &#x60;error&#x60; * &#x60;warning&#x60; * &#x60;info&#x60; | [optional] 
**used** | **int** | The number of megabytes (MB) that the account currently uses. | [optional] 

## Example

```python
from clientapi_cpanel.models.edit_user_subaccount_base_issues import EditUserSubaccountBaseIssues

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSubaccountBaseIssues from a JSON string
edit_user_subaccount_base_issues_instance = EditUserSubaccountBaseIssues.from_json(json)
# print the JSON string representation of the object
print(EditUserSubaccountBaseIssues.to_json())

# convert the object into a dict
edit_user_subaccount_base_issues_dict = edit_user_subaccount_base_issues_instance.to_dict()
# create an instance of EditUserSubaccountBaseIssues from a dict
edit_user_subaccount_base_issues_from_dict = EditUserSubaccountBaseIssues.from_dict(edit_user_subaccount_base_issues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200532ResultIssues


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
from clientapi_cpanel.models.inline_response200532_result_issues import InlineResponse200532ResultIssues

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200532ResultIssues from a JSON string
inline_response200532_result_issues_instance = InlineResponse200532ResultIssues.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200532ResultIssues.to_json())

# convert the object into a dict
inline_response200532_result_issues_dict = inline_response200532_result_issues_instance.to_dict()
# create an instance of InlineResponse200532ResultIssues from a dict
inline_response200532_result_issues_from_dict = InlineResponse200532ResultIssues.from_dict(inline_response200532_result_issues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



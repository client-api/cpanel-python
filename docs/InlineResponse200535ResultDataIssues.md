# InlineResponse200535ResultDataIssues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | The affected section of cPanel &amp; WHM. | [optional] 
**limit** | **int** | The set quota megabyte (MB) limit for the affected subaccount. | [optional] 
**message** | **str** | The description of the issue. | [optional] 
**service** | **str** | The affected service. * &#x60;email&#x60; * &#x60;ftp&#x60; * &#x60;webdisk&#x60; | [optional] 
**type** | **str** | The type of issue.  * &#x60;error&#x60; * &#x60;warning&#x60; * &#x60;info&#x60; | [optional] 
**used** | **int** | The number of megabytes (MB) that the account currently uses. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200535_result_data_issues import InlineResponse200535ResultDataIssues

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200535ResultDataIssues from a JSON string
inline_response200535_result_data_issues_instance = InlineResponse200535ResultDataIssues.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200535ResultDataIssues.to_json())

# convert the object into a dict
inline_response200535_result_data_issues_dict = inline_response200535_result_data_issues_instance.to_dict()
# create an instance of InlineResponse200535ResultDataIssues from a dict
inline_response200535_result_data_issues_from_dict = InlineResponse200535ResultDataIssues.from_dict(inline_response200535_result_data_issues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



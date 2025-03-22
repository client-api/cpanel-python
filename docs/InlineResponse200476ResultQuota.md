# InlineResponse200476ResultQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_space** | **int** | The amount of space available in megabytes (MB). | [optional] 
**can_backup** | **float** | Whether the document root has enough space to make a backup. * &#x60;1&#x60; - There is enough space. * &#x60;0&#x60; - There is not enough space. | [optional] 
**is_empty_docroot** | **float** | Whether the document root is empty. * &#x60;1&#x60; - Document root is empty. * &#x60;0&#x60; - Document root is not empty. | [optional] 
**required_space** | **int** | The amount of space required in megabytes (MB) for a document root backup. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200476_result_quota import InlineResponse200476ResultQuota

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200476ResultQuota from a JSON string
inline_response200476_result_quota_instance = InlineResponse200476ResultQuota.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200476ResultQuota.to_json())

# convert the object into a dict
inline_response200476_result_quota_dict = inline_response200476_result_quota_instance.to_dict()
# create an instance of InlineResponse200476ResultQuota from a dict
inline_response200476_result_quota_from_dict = InlineResponse200476ResultQuota.from_dict(inline_response200476_result_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



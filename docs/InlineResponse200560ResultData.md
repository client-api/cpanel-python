# InlineResponse200560ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | The unique ID of the backup process. | [optional] 
**is_running** | **int** | Whether a backup is active. * &#x60;1&#x60; - Backup in progress. * &#x60;0&#x60; - No backup in progress. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200560_result_data import InlineResponse200560ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200560ResultData from a JSON string
inline_response200560_result_data_instance = InlineResponse200560ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200560ResultData.to_json())

# convert the object into a dict
inline_response200560_result_data_dict = inline_response200560_result_data_instance.to_dict()
# create an instance of InlineResponse200560ResultData from a dict
inline_response200560_result_data_from_dict = InlineResponse200560ResultData.from_dict(inline_response200560_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



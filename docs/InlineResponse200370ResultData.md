# InlineResponse200370ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sse_url** | **str** | The SSE URI to track the progress of the process. | [optional] 
**task_id** | **str** | The task id of the SSE process. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200370_result_data import InlineResponse200370ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200370ResultData from a JSON string
inline_response200370_result_data_instance = InlineResponse200370ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200370ResultData.to_json())

# convert the object into a dict
inline_response200370_result_data_dict = inline_response200370_result_data_instance.to_dict()
# create an instance of InlineResponse200370ResultData from a dict
inline_response200370_result_data_from_dict = InlineResponse200370ResultData.from_dict(inline_response200370_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



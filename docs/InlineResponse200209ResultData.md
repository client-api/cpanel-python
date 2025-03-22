# InlineResponse200209ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace** | **str** | A series of messages that describe the trace results.  **Note:**  This output may contain HTML. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200209_result_data import InlineResponse200209ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200209ResultData from a JSON string
inline_response200209_result_data_instance = InlineResponse200209ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200209ResultData.to_json())

# convert the object into a dict
inline_response200209_result_data_dict = inline_response200209_result_data_instance.to_dict()
# create an instance of InlineResponse200209ResultData from a dict
inline_response200209_result_data_from_dict = InlineResponse200209ResultData.from_dict(inline_response200209_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



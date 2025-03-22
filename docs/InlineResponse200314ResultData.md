# InlineResponse200314ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** | Any errors that the function encounters. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200314_result_data import InlineResponse200314ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200314ResultData from a JSON string
inline_response200314_result_data_instance = InlineResponse200314ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200314ResultData.to_json())

# convert the object into a dict
inline_response200314_result_data_dict = inline_response200314_result_data_instance.to_dict()
# create an instance of InlineResponse200314ResultData from a dict
inline_response200314_result_data_from_dict = InlineResponse200314ResultData.from_dict(inline_response200314_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200289ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vhosts** | **List[str]** | The names of the changed virtual hosts. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200289_result_data import InlineResponse200289ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200289ResultData from a JSON string
inline_response200289_result_data_instance = InlineResponse200289ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200289ResultData.to_json())

# convert the object into a dict
inline_response200289_result_data_dict = inline_response200289_result_data_instance.to_dict()
# create an instance of InlineResponse200289ResultData from a dict
inline_response200289_result_data_from_dict = InlineResponse200289ResultData.from_dict(inline_response200289_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200421ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The certificate&#39;s hostname. | [optional] 
**problem** | **str** | text description of the problem. | [optional] 
**time** | **str** | When the problem occurred. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200421_result_data import InlineResponse200421ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200421ResultData from a JSON string
inline_response200421_result_data_instance = InlineResponse200421ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200421ResultData.to_json())

# convert the object into a dict
inline_response200421_result_data_dict = inline_response200421_result_data_instance.to_dict()
# create an instance of InlineResponse200421ResultData from a dict
inline_response200421_result_data_from_dict = InlineResponse200421ResultData.from_dict(inline_response200421_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



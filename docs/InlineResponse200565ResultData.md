# InlineResponse200565ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | [**InlineResponse200565ResultDataAfter**](InlineResponse200565ResultDataAfter.md) |  | [optional] 
**before** | [**InlineResponse200565ResultDataBefore**](InlineResponse200565ResultDataBefore.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200565_result_data import InlineResponse200565ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200565ResultData from a JSON string
inline_response200565_result_data_instance = InlineResponse200565ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200565ResultData.to_json())

# convert the object into a dict
inline_response200565_result_data_dict = inline_response200565_result_data_instance.to_dict()
# create an instance of InlineResponse200565ResultData from a dict
inline_response200565_result_data_from_dict = InlineResponse200565ResultData.from_dict(inline_response200565_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



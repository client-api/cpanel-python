# InlineResponse200329ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**InlineResponse200329ResultDataDomain**](InlineResponse200329ResultDataDomain.md) |  | [optional] 
**url** | **str** | The redirect&#39;s URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200329_result_data import InlineResponse200329ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200329ResultData from a JSON string
inline_response200329_result_data_instance = InlineResponse200329ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200329ResultData.to_json())

# convert the object into a dict
inline_response200329_result_data_dict = inline_response200329_result_data_instance.to_dict()
# create an instance of InlineResponse200329ResultData from a dict
inline_response200329_result_data_from_dict = InlineResponse200329ResultData.from_dict(inline_response200329_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



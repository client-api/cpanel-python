# InlineResponse200422ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | **str** | The CA bundle&#39;s tag. | [optional] 
**cab** | **str** | The CA bundle&#39;s contents. | [optional] 
**domain** | **str** | The certificate&#39;s hostname. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200422_result_data import InlineResponse200422ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200422ResultData from a JSON string
inline_response200422_result_data_instance = InlineResponse200422ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200422ResultData.to_json())

# convert the object into a dict
inline_response200422_result_data_dict = inline_response200422_result_data_instance.to_dict()
# create an instance of InlineResponse200422ResultData from a dict
inline_response200422_result_data_from_dict = InlineResponse200422ResultData.from_dict(inline_response200422_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



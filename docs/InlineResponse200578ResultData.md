# InlineResponse200578ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The cPAddon&#39;s name. | [optional] 
**module** | **str** | The module&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200578_result_data import InlineResponse200578ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200578ResultData from a JSON string
inline_response200578_result_data_instance = InlineResponse200578ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200578ResultData.to_json())

# convert the object into a dict
inline_response200578_result_data_dict = inline_response200578_result_data_instance.to_dict()
# create an instance of InlineResponse200578ResultData from a dict
inline_response200578_result_data_from_dict = InlineResponse200578ResultData.from_dict(inline_response200578_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



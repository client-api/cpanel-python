# InlineResponse20067ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | An absolute path to the infected file on the system. | [optional] 
**virus_type** | **str** | A virus type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20067_result_data import InlineResponse20067ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20067ResultData from a JSON string
inline_response20067_result_data_instance = InlineResponse20067ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20067ResultData.to_json())

# convert the object into a dict
inline_response20067_result_data_dict = inline_response20067_result_data_instance.to_dict()
# create an instance of InlineResponse20067ResultData from a dict
inline_response20067_result_data_from_dict = InlineResponse20067ResultData.from_dict(inline_response20067_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



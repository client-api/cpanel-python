# InlineResponse20057ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InlineResponse20057ResultDataResults]**](InlineResponse20057ResultDataResults.md) | The results for each attempted add operation. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20057_result_data import InlineResponse20057ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20057ResultData from a JSON string
inline_response20057_result_data_instance = InlineResponse20057ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20057ResultData.to_json())

# convert the object into a dict
inline_response20057_result_data_dict = inline_response20057_result_data_instance.to_dict()
# create an instance of InlineResponse20057ResultData from a dict
inline_response20057_result_data_from_dict = InlineResponse20057ResultData.from_dict(inline_response20057_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



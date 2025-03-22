# InlineResponse200165ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[InlineResponse200165ResultDataActions]**](InlineResponse200165ResultDataActions.md) | An array of objects that contains the filter&#39;s actions. | [optional] 
**filtername** | **str** | The filter&#39;s name. | [optional] 
**metadata** | [**InlineResponse200165ResultDataMetadata**](InlineResponse200165ResultDataMetadata.md) |  | [optional] 
**rules** | [**List[InlineResponse200165ResultDataRules]**](InlineResponse200165ResultDataRules.md) | An array of objects that contains the filter&#39;s rules. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200165_result_data import InlineResponse200165ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200165ResultData from a JSON string
inline_response200165_result_data_instance = InlineResponse200165ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200165ResultData.to_json())

# convert the object into a dict
inline_response200165_result_data_dict = inline_response200165_result_data_instance.to_dict()
# create an instance of InlineResponse200165ResultData from a dict
inline_response200165_result_data_from_dict = InlineResponse200165ResultData.from_dict(inline_response200165_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



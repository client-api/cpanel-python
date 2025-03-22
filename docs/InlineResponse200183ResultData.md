# InlineResponse200183ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[InlineResponse200183ResultActions]**](InlineResponse200183ResultActions.md) | An array of objects that descibe each of the filter’s actions. | [optional] 
**enabled** | **int** | Whether the filter is enabled. | [optional] 
**filtername** | **str** | The filter’s name. | [optional] 
**rules** | [**List[InlineResponse200183ResultRules]**](InlineResponse200183ResultRules.md) | An array of objects that descibe each of the filter’s rules. | [optional] 
**unescaped** | **bool** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200183_result_data import InlineResponse200183ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200183ResultData from a JSON string
inline_response200183_result_data_instance = InlineResponse200183ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200183ResultData.to_json())

# convert the object into a dict
inline_response200183_result_data_dict = inline_response200183_result_data_instance.to_dict()
# create an instance of InlineResponse200183ResultData from a dict
inline_response200183_result_data_from_dict = InlineResponse200183ResultData.from_dict(inline_response200183_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



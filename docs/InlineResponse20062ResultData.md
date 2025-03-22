# InlineResponse20062ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**footer** | **str** | The pages&#39; footer. | [optional] 
**header** | **str** | The pages&#39; header. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20062_result_data import InlineResponse20062ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20062ResultData from a JSON string
inline_response20062_result_data_instance = InlineResponse20062ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20062ResultData.to_json())

# convert the object into a dict
inline_response20062_result_data_dict = inline_response20062_result_data_instance.to_dict()
# create an instance of InlineResponse20062ResultData from a dict
inline_response20062_result_data_from_dict = InlineResponse20062ResultData.from_dict(inline_response20062_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



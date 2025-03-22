# InlineResponse20077ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether Horde is enabled. Always false because horde is no longer installed with the product. * &#x60;0&#x60; — Disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20077_result_data import InlineResponse20077ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20077ResultData from a JSON string
inline_response20077_result_data_instance = InlineResponse20077ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20077ResultData.to_json())

# convert the object into a dict
inline_response20077_result_data_dict = inline_response20077_result_data_instance.to_dict()
# create an instance of InlineResponse20077ResultData from a dict
inline_response20077_result_data_from_dict = InlineResponse20077ResultData.from_dict(inline_response20077_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



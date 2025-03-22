# InlineResponse20055ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **int** | Whether the sharing removal succeeded. * &#x60;1&#x60; — Removed. * &#x60;0&#x60; — **Not** removed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20055_result_data import InlineResponse20055ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20055ResultData from a JSON string
inline_response20055_result_data_instance = InlineResponse20055ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20055ResultData.to_json())

# convert the object into a dict
inline_response20055_result_data_dict = inline_response20055_result_data_instance.to_dict()
# create an instance of InlineResponse20055ResultData from a dict
inline_response20055_result_data_from_dict = InlineResponse20055ResultData.from_dict(inline_response20055_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



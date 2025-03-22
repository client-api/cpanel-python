# InlineResponse20054ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **int** | Whether the operation succeeded. * &#x60;1&#x60; — Operation succeeded. * &#x60;0&#x60; — Operation did **not** succeed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20054_result_data import InlineResponse20054ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20054ResultData from a JSON string
inline_response20054_result_data_instance = InlineResponse20054ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20054ResultData.to_json())

# convert the object into a dict
inline_response20054_result_data_dict = inline_response20054_result_data_instance.to_dict()
# create an instance of InlineResponse20054ResultData from a dict
inline_response20054_result_data_from_dict = InlineResponse20054ResultData.from_dict(inline_response20054_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



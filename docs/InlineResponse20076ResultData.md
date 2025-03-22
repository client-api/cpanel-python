# InlineResponse20076ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the DAV service is enabled. * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — Disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20076_result_data import InlineResponse20076ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20076ResultData from a JSON string
inline_response20076_result_data_instance = InlineResponse20076ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20076ResultData.to_json())

# convert the object into a dict
inline_response20076_result_data_dict = inline_response20076_result_data_instance.to_dict()
# create an instance of InlineResponse20076ResultData from a dict
inline_response20076_result_data_from_dict = InlineResponse20076ResultData.from_dict(inline_response20076_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



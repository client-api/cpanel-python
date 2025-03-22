# InlineResponse200434ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether SNI for mail is enabled. * &#x60;1&#x60; - SNI is enabled. * &#x60;0&#x60; - SNI is **not** enabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200434_result_data import InlineResponse200434ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200434ResultData from a JSON string
inline_response200434_result_data_instance = InlineResponse200434ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200434ResultData.to_json())

# convert the object into a dict
inline_response200434_result_data_dict = inline_response200434_result_data_instance.to_dict()
# create an instance of InlineResponse200434ResultData from a dict
inline_response200434_result_data_from_dict = InlineResponse200434ResultData.from_dict(inline_response200434_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



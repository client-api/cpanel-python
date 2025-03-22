# InlineResponse200144ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtername** | **str** | The filter&#39;s name. The filtername input parameter&#39;s value. | [optional] 
**updated** | **int** | Whether the function updated the filter. * &#x60;1&#x60; - Updated, * &#x60;0&#x60; - Did **not** update. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200144_result_data import InlineResponse200144ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200144ResultData from a JSON string
inline_response200144_result_data_instance = InlineResponse200144ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200144ResultData.to_json())

# convert the object into a dict
inline_response200144_result_data_dict = inline_response200144_result_data_instance.to_dict()
# create an instance of InlineResponse200144ResultData from a dict
inline_response200144_result_data_from_dict = InlineResponse200144ResultData.from_dict(inline_response200144_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



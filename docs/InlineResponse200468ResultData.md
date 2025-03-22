# InlineResponse200468ResultData

An object that contains information about the user's activation code validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Whether the user&#39;s activation code is valid. * &#x60;1&#x60; - Valid. * &#x60;0&#x60; - Invalid. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200468_result_data import InlineResponse200468ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200468ResultData from a JSON string
inline_response200468_result_data_instance = InlineResponse200468ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200468ResultData.to_json())

# convert the object into a dict
inline_response200468_result_data_dict = inline_response200468_result_data_instance.to_dict()
# create an instance of InlineResponse200468ResultData from a dict
inline_response200468_result_data_from_dict = InlineResponse200468ResultData.from_dict(inline_response200468_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



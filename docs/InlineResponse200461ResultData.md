# InlineResponse200461ResultData

An object that contains whether the user has been deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **int** | Whether or not the account has been successfully deleted. * &#x60;1&#x60; - Success * &#x60;0&#x60; - Failed | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200461_result_data import InlineResponse200461ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200461ResultData from a JSON string
inline_response200461_result_data_instance = InlineResponse200461ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200461ResultData.to_json())

# convert the object into a dict
inline_response200461_result_data_dict = inline_response200461_result_data_instance.to_dict()
# create an instance of InlineResponse200461ResultData from a dict
inline_response200461_result_data_from_dict = InlineResponse200461ResultData.from_dict(inline_response200461_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



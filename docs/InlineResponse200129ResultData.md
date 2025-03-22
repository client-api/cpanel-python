# InlineResponse200129ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkmx** | [**InlineResponse200125ResultDataCheckmx**](InlineResponse200125ResultDataCheckmx.md) |  | [optional] 
**results** | **str** | A message of success, or an error message. * A message of success that begins with &#x60;Added entry:&#x60;. * An error message. | [optional] 
**status** | **int** | Whether the function succeeded. * &#x60;1&#x60; - Success. * &#x60;0&#x60; - Failure. | [optional] 
**statusmsg** | **str** | A message of success, or an error message. * A message of success that begins with &#x60;Added entry:&#x60;. * An error message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200129_result_data import InlineResponse200129ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200129ResultData from a JSON string
inline_response200129_result_data_instance = InlineResponse200129ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200129ResultData.to_json())

# convert the object into a dict
inline_response200129_result_data_dict = inline_response200129_result_data_instance.to_dict()
# create an instance of InlineResponse200129ResultData from a dict
inline_response200129_result_data_from_dict = InlineResponse200129ResultData.from_dict(inline_response200129_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200521ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otpauth_str** | **str** | A one-time authentication URL to encode as the QR code. | [optional] 
**secret** | **str** | A generated code for use with two-factor authentication. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200521_result_data import InlineResponse200521ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200521ResultData from a JSON string
inline_response200521_result_data_instance = InlineResponse200521ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200521ResultData.to_json())

# convert the object into a dict
inline_response200521_result_data_dict = inline_response200521_result_data_instance.to_dict()
# create an instance of InlineResponse200521ResultData from a dict
inline_response200521_result_data_from_dict = InlineResponse200521ResultData.from_dict(inline_response200521_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



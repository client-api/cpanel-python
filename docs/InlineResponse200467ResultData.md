# InlineResponse200467ResultData

An object that contains the activation email request status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_activation_email** | **int** | Whether the request to send an activation email was successful. * &#x60;1&#x60; - The request was successful. An activation email will send. * &#x60;0&#x60; - The request was not successful. An activation email will not send. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200467_result_data import InlineResponse200467ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200467ResultData from a JSON string
inline_response200467_result_data_instance = InlineResponse200467ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200467ResultData.to_json())

# convert the object into a dict
inline_response200467_result_data_dict = inline_response200467_result_data_instance.to_dict()
# create an instance of InlineResponse200467ResultData from a dict
inline_response200467_result_data_from_dict = InlineResponse200467ResultData.from_dict(inline_response200467_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



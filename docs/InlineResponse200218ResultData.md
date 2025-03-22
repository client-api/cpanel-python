# InlineResponse200218ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for which the system confirmed that a valid DKIM key exists. | [optional] 
**msg** | **str** | The domain&#39;s DKIM key status message. | [optional] 
**status** | **int** | Whether the system verified that the domain&#39;s DKIM key exists. * &#x60;1&#x60; - The system verified the existence of the domain&#39;s DKIM key. * &#x60;0&#x60; - The system did **not** verify the existence of the domain&#39;s DKIM key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200218_result_data import InlineResponse200218ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200218ResultData from a JSON string
inline_response200218_result_data_instance = InlineResponse200218ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200218ResultData.to_json())

# convert the object into a dict
inline_response200218_result_data_dict = inline_response200218_result_data_instance.to_dict()
# create an instance of InlineResponse200218ResultData from a dict
inline_response200218_result_data_from_dict = InlineResponse200218ResultData.from_dict(inline_response200218_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



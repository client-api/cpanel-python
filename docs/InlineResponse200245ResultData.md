# InlineResponse200245ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allows** | **int** | Whether the cPanel account allows inbound anonymous FTP transfers. * &#x60;1&#x60; - Allowed. * &#x60;0&#x60; - Not allowed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200245_result_data import InlineResponse200245ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200245ResultData from a JSON string
inline_response200245_result_data_instance = InlineResponse200245ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200245ResultData.to_json())

# convert the object into a dict
inline_response200245_result_data_dict = inline_response200245_result_data_instance.to_dict()
# create an instance of InlineResponse200245ResultData from a dict
inline_response200245_result_data_from_dict = InlineResponse200245ResultData.from_dict(inline_response200245_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



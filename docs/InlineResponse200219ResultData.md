# InlineResponse200219ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The queried domain. | [optional] 
**pem** | **str** | The domain&#39;s DKIM private key, in PEM format. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200219_result_data import InlineResponse200219ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200219ResultData from a JSON string
inline_response200219_result_data_instance = InlineResponse200219ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200219ResultData.to_json())

# convert the object into a dict
inline_response200219_result_data_dict = inline_response200219_result_data_instance.to_dict()
# create an instance of InlineResponse200219ResultData from a dict
inline_response200219_result_data_from_dict = InlineResponse200219ResultData.from_dict(inline_response200219_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



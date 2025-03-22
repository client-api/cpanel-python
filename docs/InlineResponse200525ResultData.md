# InlineResponse200525ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tfa_configured** | **int** | Whether two-factor authentication is enabled. * &#x60;1&#x60; - Enabled. * &#x60;1&#x60; - Disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200525_result_data import InlineResponse200525ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200525ResultData from a JSON string
inline_response200525_result_data_instance = InlineResponse200525ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200525ResultData.to_json())

# convert the object into a dict
inline_response200525_result_data_dict = inline_response200525_result_data_instance.to_dict()
# create an instance of InlineResponse200525ResultData from a dict
inline_response200525_result_data_from_dict = InlineResponse200525ResultData.from_dict(inline_response200525_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



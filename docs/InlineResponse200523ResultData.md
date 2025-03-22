# InlineResponse200523ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **int** | Whether two-factor authentication is enabled for the account. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled. | [optional] 
**issuer** | **str** | The authentication code issuer&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200523_result_data import InlineResponse200523ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200523ResultData from a JSON string
inline_response200523_result_data_instance = InlineResponse200523ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200523ResultData.to_json())

# convert the object into a dict
inline_response200523_result_data_dict = inline_response200523_result_data_instance.to_dict()
# create an instance of InlineResponse200523ResultData from a dict
inline_response200523_result_data_from_dict = InlineResponse200523ResultData.from_dict(inline_response200523_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



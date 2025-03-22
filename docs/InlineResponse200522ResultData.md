# InlineResponse200522ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **int** | Whether two-factor authentication is enabled for the team user. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled. | [optional] 
**issuer** | **str** | The authentication code issuer&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200522_result_data import InlineResponse200522ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200522ResultData from a JSON string
inline_response200522_result_data_instance = InlineResponse200522ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200522ResultData.to_json())

# convert the object into a dict
inline_response200522_result_data_dict = inline_response200522_result_data_instance.to_dict()
# create an instance of InlineResponse200522ResultData from a dict
inline_response200522_result_data_from_dict = InlineResponse200522ResultData.from_dict(inline_response200522_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



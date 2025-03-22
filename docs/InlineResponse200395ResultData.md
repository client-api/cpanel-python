# InlineResponse200395ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The cPanel account&#39;s domain. | [optional] 
**select** | **str** | Whether the cPanel account&#39;s user is currently logged in.  * &#x60;1&#x60; — Logged in. * An empty string — **Not** logged in. | [optional] 
**user** | **str** | The cPanel account&#39;s username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200395_result_data import InlineResponse200395ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200395ResultData from a JSON string
inline_response200395_result_data_instance = InlineResponse200395ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200395ResultData.to_json())

# convert the object into a dict
inline_response200395_result_data_dict = inline_response200395_result_data_instance.to_dict()
# create an instance of InlineResponse200395ResultData from a dict
inline_response200395_result_data_from_dict = InlineResponse200395ResultData.from_dict(inline_response200395_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



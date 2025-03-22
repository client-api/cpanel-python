# InlineResponse200466ResultData

An object that contains the status of the account data removal from the cPanel user's configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset** | **int** | Whether the account data was removed. * &#x60;1&#x60; - The account data was removed. * &#x60;0&#x60; - The account data was not removed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200466_result_data import InlineResponse200466ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200466ResultData from a JSON string
inline_response200466_result_data_instance = InlineResponse200466ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200466ResultData.to_json())

# convert the object into a dict
inline_response200466_result_data_dict = inline_response200466_result_data_instance.to_dict()
# create an instance of InlineResponse200466ResultData from a dict
inline_response200466_result_data_from_dict = InlineResponse200466ResultData.from_dict(inline_response200466_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



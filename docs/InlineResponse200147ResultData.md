# InlineResponse200147ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spam_auto_delete** | **int** | Whether the auto-delete spam feature is disabled. &#x60;0&#x60; is the **only** possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200147_result_data import InlineResponse200147ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200147ResultData from a JSON string
inline_response200147_result_data_instance = InlineResponse200147ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200147ResultData.to_json())

# convert the object into a dict
inline_response200147_result_data_dict = inline_response200147_result_data_instance.to_dict()
# create an instance of InlineResponse200147ResultData from a dict
inline_response200147_result_data_from_dict = InlineResponse200147ResultData.from_dict(inline_response200147_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



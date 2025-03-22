# InlineResponse200315ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token that returns from the code parameter after you log in. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200315_result_data import InlineResponse200315ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200315ResultData from a JSON string
inline_response200315_result_data_instance = InlineResponse200315ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200315ResultData.to_json())

# convert the object into a dict
inline_response200315_result_data_dict = inline_response200315_result_data_instance.to_dict()
# create an instance of InlineResponse200315ResultData from a dict
inline_response200315_result_data_from_dict = InlineResponse200315ResultData.from_dict(inline_response200315_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



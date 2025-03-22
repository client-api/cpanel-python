# InlineResponse200101ResultDataHomeState

An object containing the home directory's indexing information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_type** | [**IndexType**](IndexType.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101_result_data_home_state import InlineResponse200101ResultDataHomeState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101ResultDataHomeState from a JSON string
inline_response200101_result_data_home_state_instance = InlineResponse200101ResultDataHomeState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101ResultDataHomeState.to_json())

# convert the object into a dict
inline_response200101_result_data_home_state_dict = inline_response200101_result_data_home_state_instance.to_dict()
# create an instance of InlineResponse200101ResultDataHomeState from a dict
inline_response200101_result_data_home_state_from_dict = InlineResponse200101ResultDataHomeState.from_dict(inline_response200101_result_data_home_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200101ResultDataHome

The user's home directory and its indexing information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The home directory&#39;s absolute path. | [optional] 
**state** | [**InlineResponse200101ResultDataHomeState**](InlineResponse200101ResultDataHomeState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101_result_data_home import InlineResponse200101ResultDataHome

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101ResultDataHome from a JSON string
inline_response200101_result_data_home_instance = InlineResponse200101ResultDataHome.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101ResultDataHome.to_json())

# convert the object into a dict
inline_response200101_result_data_home_dict = inline_response200101_result_data_home_instance.to_dict()
# create an instance of InlineResponse200101ResultDataHome from a dict
inline_response200101_result_data_home_from_dict = InlineResponse200101ResultDataHome.from_dict(inline_response200101_result_data_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



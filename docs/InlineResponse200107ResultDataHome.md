# InlineResponse200107ResultDataHome

The user's home directory and its privacy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The home directory&#39;s absolute path. | [optional] 
**state** | [**InlineResponse200107ResultDataHomeState**](InlineResponse200107ResultDataHomeState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200107_result_data_home import InlineResponse200107ResultDataHome

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200107ResultDataHome from a JSON string
inline_response200107_result_data_home_instance = InlineResponse200107ResultDataHome.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200107ResultDataHome.to_json())

# convert the object into a dict
inline_response200107_result_data_home_dict = inline_response200107_result_data_home_instance.to_dict()
# create an instance of InlineResponse200107ResultDataHome from a dict
inline_response200107_result_data_home_from_dict = InlineResponse200107ResultDataHome.from_dict(inline_response200107_result_data_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



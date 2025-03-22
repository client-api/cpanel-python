# InlineResponse200109ResultDataHome

The user's `home` directory and its leech protection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The &#x60;home&#x60; directory&#39;s absolute directory path. | [optional] 
**state** | [**InlineResponse200109ResultDataHomeState**](InlineResponse200109ResultDataHomeState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_home import InlineResponse200109ResultDataHome

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataHome from a JSON string
inline_response200109_result_data_home_instance = InlineResponse200109ResultDataHome.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataHome.to_json())

# convert the object into a dict
inline_response200109_result_data_home_dict = inline_response200109_result_data_home_instance.to_dict()
# create an instance of InlineResponse200109ResultDataHome from a dict
inline_response200109_result_data_home_from_dict = InlineResponse200109ResultDataHome.from_dict(inline_response200109_result_data_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200223


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200223Result**](InlineResponse200223Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200223 import InlineResponse200223

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200223 from a JSON string
inline_response200223_instance = InlineResponse200223.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200223.to_json())

# convert the object into a dict
inline_response200223_dict = inline_response200223_instance.to_dict()
# create an instance of InlineResponse200223 from a dict
inline_response200223_from_dict = InlineResponse200223.from_dict(inline_response200223_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



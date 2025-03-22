# InlineResponse200117


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200117Result**](InlineResponse200117Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200117 import InlineResponse200117

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200117 from a JSON string
inline_response200117_instance = InlineResponse200117.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200117.to_json())

# convert the object into a dict
inline_response200117_dict = inline_response200117_instance.to_dict()
# create an instance of InlineResponse200117 from a dict
inline_response200117_from_dict = InlineResponse200117.from_dict(inline_response200117_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



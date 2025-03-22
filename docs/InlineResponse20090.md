# InlineResponse20090


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20090Result**](InlineResponse20090Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20090 import InlineResponse20090

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20090 from a JSON string
inline_response20090_instance = InlineResponse20090.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20090.to_json())

# convert the object into a dict
inline_response20090_dict = inline_response20090_instance.to_dict()
# create an instance of InlineResponse20090 from a dict
inline_response20090_from_dict = InlineResponse20090.from_dict(inline_response20090_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



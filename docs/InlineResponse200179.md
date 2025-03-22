# InlineResponse200179


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200120Result**](InlineResponse200120Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200179 import InlineResponse200179

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200179 from a JSON string
inline_response200179_instance = InlineResponse200179.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200179.to_json())

# convert the object into a dict
inline_response200179_dict = inline_response200179_instance.to_dict()
# create an instance of InlineResponse200179 from a dict
inline_response200179_from_dict = InlineResponse200179.from_dict(inline_response200179_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



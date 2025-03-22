# InlineResponse200242


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200242Result**](InlineResponse200242Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200242 import InlineResponse200242

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200242 from a JSON string
inline_response200242_instance = InlineResponse200242.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200242.to_json())

# convert the object into a dict
inline_response200242_dict = inline_response200242_instance.to_dict()
# create an instance of InlineResponse200242 from a dict
inline_response200242_from_dict = InlineResponse200242.from_dict(inline_response200242_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



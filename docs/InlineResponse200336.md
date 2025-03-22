# InlineResponse200336


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200336Result**](InlineResponse200336Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200336 import InlineResponse200336

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200336 from a JSON string
inline_response200336_instance = InlineResponse200336.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200336.to_json())

# convert the object into a dict
inline_response200336_dict = inline_response200336_instance.to_dict()
# create an instance of InlineResponse200336 from a dict
inline_response200336_from_dict = InlineResponse200336.from_dict(inline_response200336_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



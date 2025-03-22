# InlineResponse200148


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200120Result**](InlineResponse200120Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200148 import InlineResponse200148

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200148 from a JSON string
inline_response200148_instance = InlineResponse200148.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200148.to_json())

# convert the object into a dict
inline_response200148_dict = inline_response200148_instance.to_dict()
# create an instance of InlineResponse200148 from a dict
inline_response200148_from_dict = InlineResponse200148.from_dict(inline_response200148_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



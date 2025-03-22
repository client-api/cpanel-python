# InlineResponse200401


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200401Result**](InlineResponse200401Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200401 import InlineResponse200401

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200401 from a JSON string
inline_response200401_instance = InlineResponse200401.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200401.to_json())

# convert the object into a dict
inline_response200401_dict = inline_response200401_instance.to_dict()
# create an instance of InlineResponse200401 from a dict
inline_response200401_from_dict = InlineResponse200401.from_dict(inline_response200401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



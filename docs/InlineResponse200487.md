# InlineResponse200487


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200487Result**](InlineResponse200487Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200487 import InlineResponse200487

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200487 from a JSON string
inline_response200487_instance = InlineResponse200487.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200487.to_json())

# convert the object into a dict
inline_response200487_dict = inline_response200487_instance.to_dict()
# create an instance of InlineResponse200487 from a dict
inline_response200487_from_dict = InlineResponse200487.from_dict(inline_response200487_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



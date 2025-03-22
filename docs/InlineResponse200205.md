# InlineResponse200205


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200205 import InlineResponse200205

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200205 from a JSON string
inline_response200205_instance = InlineResponse200205.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200205.to_json())

# convert the object into a dict
inline_response200205_dict = inline_response200205_instance.to_dict()
# create an instance of InlineResponse200205 from a dict
inline_response200205_from_dict = InlineResponse200205.from_dict(inline_response200205_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



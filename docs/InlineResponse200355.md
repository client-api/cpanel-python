# InlineResponse200355


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200355Result**](InlineResponse200355Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200355 import InlineResponse200355

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200355 from a JSON string
inline_response200355_instance = InlineResponse200355.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200355.to_json())

# convert the object into a dict
inline_response200355_dict = inline_response200355_instance.to_dict()
# create an instance of InlineResponse200355 from a dict
inline_response200355_from_dict = InlineResponse200355.from_dict(inline_response200355_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



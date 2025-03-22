# InlineResponse200541


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200541Result**](InlineResponse200541Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200541 import InlineResponse200541

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200541 from a JSON string
inline_response200541_instance = InlineResponse200541.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200541.to_json())

# convert the object into a dict
inline_response200541_dict = inline_response200541_instance.to_dict()
# create an instance of InlineResponse200541 from a dict
inline_response200541_from_dict = InlineResponse200541.from_dict(inline_response200541_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



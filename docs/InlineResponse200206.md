# InlineResponse200206


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200206Result**](InlineResponse200206Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200206 import InlineResponse200206

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200206 from a JSON string
inline_response200206_instance = InlineResponse200206.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200206.to_json())

# convert the object into a dict
inline_response200206_dict = inline_response200206_instance.to_dict()
# create an instance of InlineResponse200206 from a dict
inline_response200206_from_dict = InlineResponse200206.from_dict(inline_response200206_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



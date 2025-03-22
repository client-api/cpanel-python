# InlineResponse200559


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200559Result**](InlineResponse200559Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200559 import InlineResponse200559

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200559 from a JSON string
inline_response200559_instance = InlineResponse200559.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200559.to_json())

# convert the object into a dict
inline_response200559_dict = inline_response200559_instance.to_dict()
# create an instance of InlineResponse200559 from a dict
inline_response200559_from_dict = InlineResponse200559.from_dict(inline_response200559_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



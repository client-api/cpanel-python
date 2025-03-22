# InlineResponse200449


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200449Result**](InlineResponse200449Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200449 import InlineResponse200449

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200449 from a JSON string
inline_response200449_instance = InlineResponse200449.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200449.to_json())

# convert the object into a dict
inline_response200449_dict = inline_response200449_instance.to_dict()
# create an instance of InlineResponse200449 from a dict
inline_response200449_from_dict = InlineResponse200449.from_dict(inline_response200449_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



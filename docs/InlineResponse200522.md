# InlineResponse200522


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200522Result**](InlineResponse200522Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200522 import InlineResponse200522

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200522 from a JSON string
inline_response200522_instance = InlineResponse200522.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200522.to_json())

# convert the object into a dict
inline_response200522_dict = inline_response200522_instance.to_dict()
# create an instance of InlineResponse200522 from a dict
inline_response200522_from_dict = InlineResponse200522.from_dict(inline_response200522_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200129


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200129Result**](InlineResponse200129Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200129 import InlineResponse200129

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200129 from a JSON string
inline_response200129_instance = InlineResponse200129.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200129.to_json())

# convert the object into a dict
inline_response200129_dict = inline_response200129_instance.to_dict()
# create an instance of InlineResponse200129 from a dict
inline_response200129_from_dict = InlineResponse200129.from_dict(inline_response200129_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



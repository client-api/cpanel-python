# InlineResponse200493


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200493Result**](InlineResponse200493Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200493 import InlineResponse200493

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200493 from a JSON string
inline_response200493_instance = InlineResponse200493.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200493.to_json())

# convert the object into a dict
inline_response200493_dict = inline_response200493_instance.to_dict()
# create an instance of InlineResponse200493 from a dict
inline_response200493_from_dict = InlineResponse200493.from_dict(inline_response200493_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



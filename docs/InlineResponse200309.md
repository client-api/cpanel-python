# InlineResponse200309


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200309Result**](InlineResponse200309Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200309 import InlineResponse200309

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200309 from a JSON string
inline_response200309_instance = InlineResponse200309.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200309.to_json())

# convert the object into a dict
inline_response200309_dict = inline_response200309_instance.to_dict()
# create an instance of InlineResponse200309 from a dict
inline_response200309_from_dict = InlineResponse200309.from_dict(inline_response200309_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



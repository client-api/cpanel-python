# InlineResponse200481


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200474Result**](InlineResponse200474Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200481 import InlineResponse200481

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200481 from a JSON string
inline_response200481_instance = InlineResponse200481.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200481.to_json())

# convert the object into a dict
inline_response200481_dict = inline_response200481_instance.to_dict()
# create an instance of InlineResponse200481 from a dict
inline_response200481_from_dict = InlineResponse200481.from_dict(inline_response200481_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



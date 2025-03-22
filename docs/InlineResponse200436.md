# InlineResponse200436


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200436Result**](InlineResponse200436Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200436 import InlineResponse200436

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200436 from a JSON string
inline_response200436_instance = InlineResponse200436.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200436.to_json())

# convert the object into a dict
inline_response200436_dict = inline_response200436_instance.to_dict()
# create an instance of InlineResponse200436 from a dict
inline_response200436_from_dict = InlineResponse200436.from_dict(inline_response200436_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



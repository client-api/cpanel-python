# InlineResponse20016


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20016Result**](InlineResponse20016Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20016 import InlineResponse20016

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20016 from a JSON string
inline_response20016_instance = InlineResponse20016.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20016.to_json())

# convert the object into a dict
inline_response20016_dict = inline_response20016_instance.to_dict()
# create an instance of InlineResponse20016 from a dict
inline_response20016_from_dict = InlineResponse20016.from_dict(inline_response20016_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



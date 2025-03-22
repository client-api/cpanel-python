# InlineResponse2001


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2001Result**](InlineResponse2001Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2001 import InlineResponse2001

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2001 from a JSON string
inline_response2001_instance = InlineResponse2001.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2001.to_json())

# convert the object into a dict
inline_response2001_dict = inline_response2001_instance.to_dict()
# create an instance of InlineResponse2001 from a dict
inline_response2001_from_dict = InlineResponse2001.from_dict(inline_response2001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



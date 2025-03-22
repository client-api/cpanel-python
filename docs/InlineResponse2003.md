# InlineResponse2003


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2002Result**](InlineResponse2002Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2003 import InlineResponse2003

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2003 from a JSON string
inline_response2003_instance = InlineResponse2003.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2003.to_json())

# convert the object into a dict
inline_response2003_dict = inline_response2003_instance.to_dict()
# create an instance of InlineResponse2003 from a dict
inline_response2003_from_dict = InlineResponse2003.from_dict(inline_response2003_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



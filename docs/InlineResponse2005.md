# InlineResponse2005


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2002Result**](InlineResponse2002Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2005 import InlineResponse2005

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2005 from a JSON string
inline_response2005_instance = InlineResponse2005.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2005.to_json())

# convert the object into a dict
inline_response2005_dict = inline_response2005_instance.to_dict()
# create an instance of InlineResponse2005 from a dict
inline_response2005_from_dict = InlineResponse2005.from_dict(inline_response2005_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse2007


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2007Result**](InlineResponse2007Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2007 import InlineResponse2007

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2007 from a JSON string
inline_response2007_instance = InlineResponse2007.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2007.to_json())

# convert the object into a dict
inline_response2007_dict = inline_response2007_instance.to_dict()
# create an instance of InlineResponse2007 from a dict
inline_response2007_from_dict = InlineResponse2007.from_dict(inline_response2007_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



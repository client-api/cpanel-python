# InlineResponse2008


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2008Result**](InlineResponse2008Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2008 import InlineResponse2008

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2008 from a JSON string
inline_response2008_instance = InlineResponse2008.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2008.to_json())

# convert the object into a dict
inline_response2008_dict = inline_response2008_instance.to_dict()
# create an instance of InlineResponse2008 from a dict
inline_response2008_from_dict = InlineResponse2008.from_dict(inline_response2008_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



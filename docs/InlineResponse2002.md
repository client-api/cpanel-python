# InlineResponse2002


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse2002Result**](InlineResponse2002Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2002 import InlineResponse2002

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2002 from a JSON string
inline_response2002_instance = InlineResponse2002.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2002.to_json())

# convert the object into a dict
inline_response2002_dict = inline_response2002_instance.to_dict()
# create an instance of InlineResponse2002 from a dict
inline_response2002_from_dict = InlineResponse2002.from_dict(inline_response2002_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



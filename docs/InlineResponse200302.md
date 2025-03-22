# InlineResponse200302


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200302Result**](InlineResponse200302Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200302 import InlineResponse200302

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200302 from a JSON string
inline_response200302_instance = InlineResponse200302.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200302.to_json())

# convert the object into a dict
inline_response200302_dict = inline_response200302_instance.to_dict()
# create an instance of InlineResponse200302 from a dict
inline_response200302_from_dict = InlineResponse200302.from_dict(inline_response200302_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



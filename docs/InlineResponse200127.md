# InlineResponse200127


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200123Result**](InlineResponse200123Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200127 import InlineResponse200127

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200127 from a JSON string
inline_response200127_instance = InlineResponse200127.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200127.to_json())

# convert the object into a dict
inline_response200127_dict = inline_response200127_instance.to_dict()
# create an instance of InlineResponse200127 from a dict
inline_response200127_from_dict = InlineResponse200127.from_dict(inline_response200127_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



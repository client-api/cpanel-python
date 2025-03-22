# InlineResponse200268


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200268Result**](InlineResponse200268Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200268 import InlineResponse200268

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200268 from a JSON string
inline_response200268_instance = InlineResponse200268.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200268.to_json())

# convert the object into a dict
inline_response200268_dict = inline_response200268_instance.to_dict()
# create an instance of InlineResponse200268 from a dict
inline_response200268_from_dict = InlineResponse200268.from_dict(inline_response200268_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200440


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200440 import InlineResponse200440

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200440 from a JSON string
inline_response200440_instance = InlineResponse200440.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200440.to_json())

# convert the object into a dict
inline_response200440_dict = inline_response200440_instance.to_dict()
# create an instance of InlineResponse200440 from a dict
inline_response200440_from_dict = InlineResponse200440.from_dict(inline_response200440_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



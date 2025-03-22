# InlineResponse200524


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200524Result**](InlineResponse200524Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200524 import InlineResponse200524

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200524 from a JSON string
inline_response200524_instance = InlineResponse200524.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200524.to_json())

# convert the object into a dict
inline_response200524_dict = inline_response200524_instance.to_dict()
# create an instance of InlineResponse200524 from a dict
inline_response200524_from_dict = InlineResponse200524.from_dict(inline_response200524_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



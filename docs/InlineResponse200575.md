# InlineResponse200575


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200575Result**](InlineResponse200575Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200575 import InlineResponse200575

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200575 from a JSON string
inline_response200575_instance = InlineResponse200575.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200575.to_json())

# convert the object into a dict
inline_response200575_dict = inline_response200575_instance.to_dict()
# create an instance of InlineResponse200575 from a dict
inline_response200575_from_dict = InlineResponse200575.from_dict(inline_response200575_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



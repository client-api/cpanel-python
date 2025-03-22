# InlineResponse200101


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200101Result**](InlineResponse200101Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101 import InlineResponse200101

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101 from a JSON string
inline_response200101_instance = InlineResponse200101.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101.to_json())

# convert the object into a dict
inline_response200101_dict = inline_response200101_instance.to_dict()
# create an instance of InlineResponse200101 from a dict
inline_response200101_from_dict = InlineResponse200101.from_dict(inline_response200101_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



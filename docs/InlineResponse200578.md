# InlineResponse200578


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200578Result**](InlineResponse200578Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200578 import InlineResponse200578

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200578 from a JSON string
inline_response200578_instance = InlineResponse200578.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200578.to_json())

# convert the object into a dict
inline_response200578_dict = inline_response200578_instance.to_dict()
# create an instance of InlineResponse200578 from a dict
inline_response200578_from_dict = InlineResponse200578.from_dict(inline_response200578_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



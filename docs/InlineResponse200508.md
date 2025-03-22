# InlineResponse200508


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200498Result**](InlineResponse200498Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200508 import InlineResponse200508

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200508 from a JSON string
inline_response200508_instance = InlineResponse200508.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200508.to_json())

# convert the object into a dict
inline_response200508_dict = inline_response200508_instance.to_dict()
# create an instance of InlineResponse200508 from a dict
inline_response200508_from_dict = InlineResponse200508.from_dict(inline_response200508_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



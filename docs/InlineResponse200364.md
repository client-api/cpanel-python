# InlineResponse200364


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200361Result**](InlineResponse200361Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200364 import InlineResponse200364

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200364 from a JSON string
inline_response200364_instance = InlineResponse200364.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200364.to_json())

# convert the object into a dict
inline_response200364_dict = inline_response200364_instance.to_dict()
# create an instance of InlineResponse200364 from a dict
inline_response200364_from_dict = InlineResponse200364.from_dict(inline_response200364_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



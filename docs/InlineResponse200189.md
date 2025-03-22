# InlineResponse200189


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200189Result**](InlineResponse200189Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200189 import InlineResponse200189

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200189 from a JSON string
inline_response200189_instance = InlineResponse200189.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200189.to_json())

# convert the object into a dict
inline_response200189_dict = inline_response200189_instance.to_dict()
# create an instance of InlineResponse200189 from a dict
inline_response200189_from_dict = InlineResponse200189.from_dict(inline_response200189_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



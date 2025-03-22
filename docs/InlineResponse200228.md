# InlineResponse200228


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200228Result**](InlineResponse200228Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200228 import InlineResponse200228

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200228 from a JSON string
inline_response200228_instance = InlineResponse200228.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200228.to_json())

# convert the object into a dict
inline_response200228_dict = inline_response200228_instance.to_dict()
# create an instance of InlineResponse200228 from a dict
inline_response200228_from_dict = InlineResponse200228.from_dict(inline_response200228_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



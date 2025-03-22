# InlineResponse200230


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200230Result**](InlineResponse200230Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200230 import InlineResponse200230

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200230 from a JSON string
inline_response200230_instance = InlineResponse200230.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200230.to_json())

# convert the object into a dict
inline_response200230_dict = inline_response200230_instance.to_dict()
# create an instance of InlineResponse200230 from a dict
inline_response200230_from_dict = InlineResponse200230.from_dict(inline_response200230_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200326


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200326Result**](InlineResponse200326Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200326 import InlineResponse200326

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200326 from a JSON string
inline_response200326_instance = InlineResponse200326.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200326.to_json())

# convert the object into a dict
inline_response200326_dict = inline_response200326_instance.to_dict()
# create an instance of InlineResponse200326 from a dict
inline_response200326_from_dict = InlineResponse200326.from_dict(inline_response200326_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



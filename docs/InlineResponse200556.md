# InlineResponse200556


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200556Result**](InlineResponse200556Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200556 import InlineResponse200556

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200556 from a JSON string
inline_response200556_instance = InlineResponse200556.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200556.to_json())

# convert the object into a dict
inline_response200556_dict = inline_response200556_instance.to_dict()
# create an instance of InlineResponse200556 from a dict
inline_response200556_from_dict = InlineResponse200556.from_dict(inline_response200556_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



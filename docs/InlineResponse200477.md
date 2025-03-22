# InlineResponse200477


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200477Result**](InlineResponse200477Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200477 import InlineResponse200477

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200477 from a JSON string
inline_response200477_instance = InlineResponse200477.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200477.to_json())

# convert the object into a dict
inline_response200477_dict = inline_response200477_instance.to_dict()
# create an instance of InlineResponse200477 from a dict
inline_response200477_from_dict = InlineResponse200477.from_dict(inline_response200477_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



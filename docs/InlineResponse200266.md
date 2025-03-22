# InlineResponse200266


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20034Result**](InlineResponse20034Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200266 import InlineResponse200266

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200266 from a JSON string
inline_response200266_instance = InlineResponse200266.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200266.to_json())

# convert the object into a dict
inline_response200266_dict = inline_response200266_instance.to_dict()
# create an instance of InlineResponse200266 from a dict
inline_response200266_from_dict = InlineResponse200266.from_dict(inline_response200266_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200378


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20033Result**](InlineResponse20033Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200378 import InlineResponse200378

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200378 from a JSON string
inline_response200378_instance = InlineResponse200378.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200378.to_json())

# convert the object into a dict
inline_response200378_dict = inline_response200378_instance.to_dict()
# create an instance of InlineResponse200378 from a dict
inline_response200378_from_dict = InlineResponse200378.from_dict(inline_response200378_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



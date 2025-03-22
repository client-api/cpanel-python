# InlineResponse200362


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200361Result**](InlineResponse200361Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200362 import InlineResponse200362

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200362 from a JSON string
inline_response200362_instance = InlineResponse200362.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200362.to_json())

# convert the object into a dict
inline_response200362_dict = inline_response200362_instance.to_dict()
# create an instance of InlineResponse200362 from a dict
inline_response200362_from_dict = InlineResponse200362.from_dict(inline_response200362_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



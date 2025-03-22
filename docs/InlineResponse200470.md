# InlineResponse200470


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200470Result**](InlineResponse200470Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200470 import InlineResponse200470

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200470 from a JSON string
inline_response200470_instance = InlineResponse200470.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200470.to_json())

# convert the object into a dict
inline_response200470_dict = inline_response200470_instance.to_dict()
# create an instance of InlineResponse200470 from a dict
inline_response200470_from_dict = InlineResponse200470.from_dict(inline_response200470_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



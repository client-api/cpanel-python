# InlineResponse200100


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200100Result**](InlineResponse200100Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200100 import InlineResponse200100

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200100 from a JSON string
inline_response200100_instance = InlineResponse200100.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200100.to_json())

# convert the object into a dict
inline_response200100_dict = inline_response200100_instance.to_dict()
# create an instance of InlineResponse200100 from a dict
inline_response200100_from_dict = InlineResponse200100.from_dict(inline_response200100_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



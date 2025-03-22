# InlineResponse20099


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20099Result**](InlineResponse20099Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20099 import InlineResponse20099

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20099 from a JSON string
inline_response20099_instance = InlineResponse20099.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20099.to_json())

# convert the object into a dict
inline_response20099_dict = inline_response20099_instance.to_dict()
# create an instance of InlineResponse20099 from a dict
inline_response20099_from_dict = InlineResponse20099.from_dict(inline_response20099_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



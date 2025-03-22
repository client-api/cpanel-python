# InlineResponse200496


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200496Result**](InlineResponse200496Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200496 import InlineResponse200496

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200496 from a JSON string
inline_response200496_instance = InlineResponse200496.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200496.to_json())

# convert the object into a dict
inline_response200496_dict = inline_response200496_instance.to_dict()
# create an instance of InlineResponse200496 from a dict
inline_response200496_from_dict = InlineResponse200496.from_dict(inline_response200496_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



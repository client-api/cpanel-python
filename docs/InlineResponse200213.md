# InlineResponse200213


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200212Result**](InlineResponse200212Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200213 import InlineResponse200213

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200213 from a JSON string
inline_response200213_instance = InlineResponse200213.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200213.to_json())

# convert the object into a dict
inline_response200213_dict = inline_response200213_instance.to_dict()
# create an instance of InlineResponse200213 from a dict
inline_response200213_from_dict = InlineResponse200213.from_dict(inline_response200213_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



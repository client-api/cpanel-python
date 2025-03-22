# InlineResponse20011


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20011Result**](InlineResponse20011Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20011 import InlineResponse20011

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20011 from a JSON string
inline_response20011_instance = InlineResponse20011.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20011.to_json())

# convert the object into a dict
inline_response20011_dict = inline_response20011_instance.to_dict()
# create an instance of InlineResponse20011 from a dict
inline_response20011_from_dict = InlineResponse20011.from_dict(inline_response20011_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



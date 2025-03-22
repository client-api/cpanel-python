# InlineResponse200469ResultMeta

A set of data that gives information on the template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[InlineResponse200469ResultMetaFields]**](InlineResponse200469ResultMetaFields.md) | This array of objects shows the information for each field the user can add input in the template. | [optional] 
**information** | [**InlineResponse200469ResultMetaInformation**](InlineResponse200469ResultMetaInformation.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200469_result_meta import InlineResponse200469ResultMeta

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200469ResultMeta from a JSON string
inline_response200469_result_meta_instance = InlineResponse200469ResultMeta.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200469ResultMeta.to_json())

# convert the object into a dict
inline_response200469_result_meta_dict = inline_response200469_result_meta_instance.to_dict()
# create an instance of InlineResponse200469ResultMeta from a dict
inline_response200469_result_meta_from_dict = InlineResponse200469ResultMeta.from_dict(inline_response200469_result_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



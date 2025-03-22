# InlineResponse200469ResultMetaFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The template&#39;s ID. | [optional] 
**label** | **str** | The template&#39;s label. | [optional] 
**placeholder** | **str** | A string that temporarily takes the place of the final data. | [optional] 
**type** | **str** | The template&#39;s type. * &#x60;color&#x60; * &#x60;datetime-local&#x60; * &#x60;email&#x60; * &#x60;Medical&#x60; * &#x60;tel&#x60; * &#x60;text&#x60; * &#x60;textarea&#x60; * &#x60;url&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200469_result_meta_fields import InlineResponse200469ResultMetaFields

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200469ResultMetaFields from a JSON string
inline_response200469_result_meta_fields_instance = InlineResponse200469ResultMetaFields.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200469ResultMetaFields.to_json())

# convert the object into a dict
inline_response200469_result_meta_fields_dict = inline_response200469_result_meta_fields_instance.to_dict()
# create an instance of InlineResponse200469ResultMetaFields from a dict
inline_response200469_result_meta_fields_from_dict = InlineResponse200469ResultMetaFields.from_dict(inline_response200469_result_meta_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



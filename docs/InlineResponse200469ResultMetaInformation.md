# InlineResponse200469ResultMetaInformation

An object that provides basic template information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | The template&#39;s add date. | [optional] 
**description** | **str** | A string describing the template. | [optional] 
**id** | **str** | A template name. | [optional] 
**name** | **str** | The template&#39;s name. | [optional] 
**preview_image_path** | **str** | The preview directory path. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200469_result_meta_information import InlineResponse200469ResultMetaInformation

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200469ResultMetaInformation from a JSON string
inline_response200469_result_meta_information_instance = InlineResponse200469ResultMetaInformation.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200469ResultMetaInformation.to_json())

# convert the object into a dict
inline_response200469_result_meta_information_dict = inline_response200469_result_meta_information_instance.to_dict()
# create an instance of InlineResponse200469ResultMetaInformation from a dict
inline_response200469_result_meta_information_from_dict = InlineResponse200469ResultMetaInformation.from_dict(inline_response200469_result_meta_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



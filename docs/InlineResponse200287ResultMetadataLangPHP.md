# InlineResponse200287ResultMetadataLangPHP

An object containing the virtual host's PHP directive information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute file path to the &#x60;php.ini&#x60; file. | [optional] 
**phpversion** | **str** | The virtual host&#39;s installed version of PHP. | [optional] 
**type** | **str** | The type of &#x60;php.ini&#x60; file.  * &#x60;home&#x60; * &#x60;vhost&#x60; | [optional] 
**vhost** | **str** | The virtual host&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200287_result_metadata_lang_php import InlineResponse200287ResultMetadataLangPHP

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200287ResultMetadataLangPHP from a JSON string
inline_response200287_result_metadata_lang_php_instance = InlineResponse200287ResultMetadataLangPHP.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200287ResultMetadataLangPHP.to_json())

# convert the object into a dict
inline_response200287_result_metadata_lang_php_dict = inline_response200287_result_metadata_lang_php_instance.to_dict()
# create an instance of InlineResponse200287ResultMetadataLangPHP from a dict
inline_response200287_result_metadata_lang_php_from_dict = InlineResponse200287ResultMetadataLangPHP.from_dict(inline_response200287_result_metadata_lang_php_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



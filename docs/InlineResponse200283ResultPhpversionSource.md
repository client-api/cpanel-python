# InlineResponse200283ResultPhpversionSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain the virtual host inherits its PHP version from. | [optional] 
**system_default** | **int** | Whether the virtual host uses the system&#39;s default PHP version. * &#x60;1&#x60; - Uses the system default PHP version.  **Note:**    The function **only** returns this value if true. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200283_result_phpversion_source import InlineResponse200283ResultPhpversionSource

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200283ResultPhpversionSource from a JSON string
inline_response200283_result_phpversion_source_instance = InlineResponse200283ResultPhpversionSource.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200283ResultPhpversionSource.to_json())

# convert the object into a dict
inline_response200283_result_phpversion_source_dict = inline_response200283_result_phpversion_source_instance.to_dict()
# create an instance of InlineResponse200283ResultPhpversionSource from a dict
inline_response200283_result_phpversion_source_from_dict = InlineResponse200283ResultPhpversionSource.from_dict(inline_response200283_result_phpversion_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



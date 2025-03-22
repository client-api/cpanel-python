# InlineResponse200284ResultDataDirectives


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | [**InlineResponse200284ResultDataDirectivesDefaultValue**](InlineResponse200284ResultDataDirectivesDefaultValue.md) |  | [optional] 
**info** | **str** | The purpose of the directive. | [optional] 
**key** | **str** | The directive&#39;s name. | [optional] 
**php_ini_mode** | **str** | The directive&#39;s [PHP_INI mode](http://php.net/manual/en/configuration.changes.modes.php).  * &#x60;PHP_INI_SYSTEM&#x60; * &#x60;PHP_INI_PERDIR&#x60; * &#x60;PHP_INI_ALL&#x60; * &#x60;PHPINI_ONLY&#x60; | [optional] 
**type** | **str** | The type of value that the directive uses.  * &#x60;string&#x60; * &#x60;boolean&#x60; * &#x60;integer&#x60; * &#x60;float&#x60; | [optional] 
**value** | **str** | The directive&#39;s current value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200284_result_data_directives import InlineResponse200284ResultDataDirectives

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200284ResultDataDirectives from a JSON string
inline_response200284_result_data_directives_instance = InlineResponse200284ResultDataDirectives.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200284ResultDataDirectives.to_json())

# convert the object into a dict
inline_response200284_result_data_directives_dict = inline_response200284_result_data_directives_instance.to_dict()
# create an instance of InlineResponse200284ResultDataDirectives from a dict
inline_response200284_result_data_directives_from_dict = InlineResponse200284ResultDataDirectives.from_dict(inline_response200284_result_data_directives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



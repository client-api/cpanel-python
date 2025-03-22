# InlineResponse20092ResultDataEnabledAdditionalProperties

Information about the domain for which the system enabled DNSSEC.  **Note:**  This return's name is the `domain` parameter's value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the system enabled DNSSEC.  * &#x60;1&#x60; — The system enabled DNSSEC. * &#x60;0&#x60; — The system failed to enable DNSSEC. | [optional] 
**new_key_id** | **int** | The assigned security key ID. | [optional] 
**nsec_version** | **str** | The version of DNSSEC the system used.  * &#x60;NSEC3&#x60; * &#x60;NSEC&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20092_result_data_enabled_additional_properties import InlineResponse20092ResultDataEnabledAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20092ResultDataEnabledAdditionalProperties from a JSON string
inline_response20092_result_data_enabled_additional_properties_instance = InlineResponse20092ResultDataEnabledAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20092ResultDataEnabledAdditionalProperties.to_json())

# convert the object into a dict
inline_response20092_result_data_enabled_additional_properties_dict = inline_response20092_result_data_enabled_additional_properties_instance.to_dict()
# create an instance of InlineResponse20092ResultDataEnabledAdditionalProperties from a dict
inline_response20092_result_data_enabled_additional_properties_from_dict = InlineResponse20092ResultDataEnabledAdditionalProperties.from_dict(inline_response20092_result_data_enabled_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



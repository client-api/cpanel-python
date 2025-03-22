# InlineResponse20091ResultDataDisabled

An array of objects that contain the domains for which the system disabled DNSSEC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **int** | Information about the domains for which the system disabled DNSSEC.  * &#x60;1&#x60; — Disabled. * &#x60;0&#x60; — The system failed to disable DNSSEC.  **Note:**  This return&#39;s name is the &#x60;domain&#x60; parameter&#39;s value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20091_result_data_disabled import InlineResponse20091ResultDataDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20091ResultDataDisabled from a JSON string
inline_response20091_result_data_disabled_instance = InlineResponse20091ResultDataDisabled.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20091ResultDataDisabled.to_json())

# convert the object into a dict
inline_response20091_result_data_disabled_dict = inline_response20091_result_data_disabled_instance.to_dict()
# create an instance of InlineResponse20091ResultDataDisabled from a dict
inline_response20091_result_data_disabled_from_dict = InlineResponse20091ResultDataDisabled.from_dict(inline_response20091_result_data_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



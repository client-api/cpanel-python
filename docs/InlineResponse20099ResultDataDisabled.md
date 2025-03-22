# InlineResponse20099ResultDataDisabled

A list of the domains for which the system disabled NSEC3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **int** | Whether the system disabled NSEC3 on the domain.  * &#x60;1&#x60; — Disabled. * &#x60;0&#x60; — The system failed to disable NSEC3.  **Note:**  This return&#39;s name is the &#x60;domain&#x60; parameter&#39;s value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20099_result_data_disabled import InlineResponse20099ResultDataDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20099ResultDataDisabled from a JSON string
inline_response20099_result_data_disabled_instance = InlineResponse20099ResultDataDisabled.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20099ResultDataDisabled.to_json())

# convert the object into a dict
inline_response20099_result_data_disabled_dict = inline_response20099_result_data_disabled_instance.to_dict()
# create an instance of InlineResponse20099ResultDataDisabled from a dict
inline_response20099_result_data_disabled_from_dict = InlineResponse20099ResultDataDisabled.from_dict(inline_response20099_result_data_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



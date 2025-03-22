# InlineResponse200541ResultDataMxcheck

Domains and their mail exchanger (MX) type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **str** | The domain&#39;s MX type.  * &#x60;local&#x60; - Accept mail locally for the domain. * &#x60;remote&#x60; - Do not accept mail locally for the domain. * &#x60;secondary&#x60; - Accept mail until a higher priority mail server is available.  **Note:**  The return&#39;s name is the domain name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200541_result_data_mxcheck import InlineResponse200541ResultDataMxcheck

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200541ResultDataMxcheck from a JSON string
inline_response200541_result_data_mxcheck_instance = InlineResponse200541ResultDataMxcheck.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200541ResultDataMxcheck.to_json())

# convert the object into a dict
inline_response200541_result_data_mxcheck_dict = inline_response200541_result_data_mxcheck_instance.to_dict()
# create an instance of InlineResponse200541ResultDataMxcheck from a dict
inline_response200541_result_data_mxcheck_from_dict = InlineResponse200541ResultDataMxcheck.from_dict(inline_response200541_result_data_mxcheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



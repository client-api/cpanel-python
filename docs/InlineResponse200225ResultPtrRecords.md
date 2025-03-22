# InlineResponse200225ResultPtrRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The fully-qualified domain name (FQDN) that a PTR record points to. | [optional] 
**forward_records** | **List[str]** | A list of IP addresses that the domain resolves to for A (IPv4) and AAAA (IPv6) records. | [optional] 
**state** | **str** | The state of the domain&#39;s PTR record. * &#x60;VALID&#x60; - The PTR record is valid. * &#x60;MISSING_FWD&#x60; - The PTR points to a domain without an A or AAAA record. * &#x60;FWD_MISMATCH&#x60; - The PTR record points to a domain without an A or AAAA record that points back to the IP address. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200225_result_ptr_records import InlineResponse200225ResultPtrRecords

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200225ResultPtrRecords from a JSON string
inline_response200225_result_ptr_records_instance = InlineResponse200225ResultPtrRecords.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200225ResultPtrRecords.to_json())

# convert the object into a dict
inline_response200225_result_ptr_records_dict = inline_response200225_result_ptr_records_instance.to_dict()
# create an instance of InlineResponse200225ResultPtrRecords from a dict
inline_response200225_result_ptr_records_from_dict = InlineResponse200225ResultPtrRecords.from_dict(inline_response200225_result_ptr_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



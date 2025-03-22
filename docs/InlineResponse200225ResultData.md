# InlineResponse200225ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arpa_domain** | **str** | The IP address used to perform a reverse DNS (rDNS) lookup. For more information about rDNS, read our [How to Configure Reverse DNS for BIND in WHM](https://go.cpanel.net/HowtoConfigureReverseDNSforBINDinWHM) documentation. A valid reversed IP address appended with one of the following: * in-addr.arpa - An IPv4 address. * ip6.arpa - An IPv6 address.  For information about .arpa domains, read Wikipedia&#39;s [Reverse DNS lookup](https://en.wikipedia.org/wiki/Reverse_DNS_lookup) article.  **Note:**  The function does not return this value for a domain with an invalid IP address. | [optional] 
**domain** | **str** | The queried domain. | [optional] 
**error** | **str** | A mmessage that details the reason why the domain&#39;s IP address validation failed.  **Note:**  The function only returns this value when the &#x60;state&#x60; returned is the &#x60;ERROR&#x60; value. | [optional] 
**helo** | **str** | The hostname that the domain uses to identify itself to remote SMTP servers. A valid hostname. | [optional] 
**ip_address** | **str** | The IP address.  **Note:**  The function does **not** return this value for a domain with an invalid IP address. | [optional] 
**ip_version** | **int** | The IP version number. * 4 * 6  **Note:**  The function does **not** return this value for a domain with an invalid IP address. | [optional] 
**nameservers** | **List[str]** | The authoritative nameservers for the domain&#39;s PTR record. | [optional] 
**ptr_records** | [**List[InlineResponse200225ResultPtrRecords]**](InlineResponse200225ResultPtrRecords.md) | The domain&#39;s PTR records.  **Note:**  The function does **not** return this for a domain with an invalid IP address. | [optional] 
**state** | **str** | Whether the PTR records are valid for the domain. * &#x60;ERROR&#x60; - The domain&#39;s IP address is invalid. The function returns the reason in the error return. * &#x60;IP_IS_PRIVATE&#x60; - The IP address exists within a range of private IP addresses. * &#x60;VALID&#x60; - The PTR record is valid. * &#x60;MISSING_PTR&#x60; - No PTR records exist for the IP address. * &#x60;PTR_MISMATCH&#x60; - One or more PTR records point to a domain that does not point back to the correct IP address.  **Note:**  * DNS does not define PTR records for private IP addresses. * The function only returns a VALID response if all of an IP address&#39;s PTR records are valid. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200225_result_data import InlineResponse200225ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200225ResultData from a JSON string
inline_response200225_result_data_instance = InlineResponse200225ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200225ResultData.to_json())

# convert the object into a dict
inline_response200225_result_data_dict = inline_response200225_result_data_instance.to_dict()
# create an instance of InlineResponse200225ResultData from a dict
inline_response200225_result_data_from_dict = InlineResponse200225ResultData.from_dict(inline_response200225_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20095ResultDataAdditionalPropertiesNsecDetails

An object containing the [Next Secure Record](https://tools.ietf.org/html/rfc4470) (NSEC) information for the selected domain.  **Note:**   If the domain uses NSEC semantics, only the `nsec_version` return appears in the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nsec3_hash_algo_desc** | **str** | A description of the NSEC3 key&#39;s algorithm. | [optional] 
**nsec3_hash_algo_num** | **int** | The DNSSEC Digest Algorithm Number. | [optional] 
**nsec3_iterations** | **int** | The number of times that the system rehashes the first hash operation. | [optional] 
**nsec3_narrow** | **int** | Whether NSEC3 will operate in Narrow or Inclusive mode.  * &#x60;1&#x60; - Narrow mode. * &#x60;0&#x60; - Inclusive mode.  **Note:**   For more information about these modes, read [PowerDNS&#39;s DNSSEC documentation](https://doc.powerdns.com/authoritative/dnssec/intro.html). | [optional] 
**nsec3_opt_out** | **int** | Whether NSEC3 will create records for all delegations or only for secure delegations.  * &#x60;1&#x60; - Create records for all delegations. * &#x60;0&#x60; - Create records only for secure delegations. | [optional] 
**nsec3_salt** | **str** | The salt value that PowerDNS uses in the hashes.  **Note:**   For more information about the salt value, read [RFC 5155](https://tools.ietf.org/html/rfc5155#section-3.1.5). | [optional] 
**nsec_version** | **str** | Whether the domain uses NSEC or [Next Secure Record version 3](https://tools.ietf.org/html/rfc5155) (NSEC3) [Domain Name Security Extensions](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions) (DNSSEC) semantics.  * &#x60;NSEC&#x60; * &#x60;NSEC3&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20095_result_data_additional_properties_nsec_details import InlineResponse20095ResultDataAdditionalPropertiesNsecDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesNsecDetails from a JSON string
inline_response20095_result_data_additional_properties_nsec_details_instance = InlineResponse20095ResultDataAdditionalPropertiesNsecDetails.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20095ResultDataAdditionalPropertiesNsecDetails.to_json())

# convert the object into a dict
inline_response20095_result_data_additional_properties_nsec_details_dict = inline_response20095_result_data_additional_properties_nsec_details_instance.to_dict()
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesNsecDetails from a dict
inline_response20095_result_data_additional_properties_nsec_details_from_dict = InlineResponse20095ResultDataAdditionalPropertiesNsecDetails.from_dict(inline_response20095_result_data_additional_properties_nsec_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties

The information related to the domain's DNSSEC record.  **Note:**  The return's name is the `key_tag` return's integer value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** | Whether the DS key is active.  * &#x60;1&#x60; - Active. * &#x60;0&#x60; - Inactive. | [optional] 
**algo_desc** | **str** | A description of the algorithm that the DS key uses. | [optional] 
**algo_num** | **int** | The algorithm the system generated for the security key.  * &#x60;5&#x60; - RSA/SHA-1 * &#x60;6&#x60; - DSA-NSEC3-SHA1 * &#x60;7&#x60; - RSASHA1-NSEC3-SHA1 * &#x60;8&#x60; - RSA/SHA-256 * &#x60;10&#x60; - RSA/SHA-512 * &#x60;13&#x60; - ECDSA Curve P-256 with SHA-256 * &#x60;14&#x60; - ECDSA Curve P-384 with SHA-384 | [optional] 
**algo_tag** | **str** | The short-form reference to the algorithm. | [optional] 
**bits** | **int** | The DS key&#39;s size, in bits. | [optional] 
**created** | **int** | The key&#39;s creation time. | [optional] 
**digests** | [**List[InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests]**](InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests.md) | The information that  the registrar uses to populate the DS records. | [optional] 
**flags** | **int** | An integer that determines the &#x60;key_type&#x60; value.  * &#x60;256&#x60; - A Zone Signing Key (ZSK). * &#x60;257&#x60; - A Combined Signing Key (CSK) or Key Signing Key (KSK). | [optional] 
**key_id** | **int** | PowerDNS&#39;s internal identifier. | [optional] 
**key_tag** | **int** | The DS key&#39;s identification number. | [optional] 
**key_type** | **str** | The DS key&#39;s signing type. * &#x60;CSK&#x60; - Combined Signing Key. * &#x60;KSK&#x60; - Key Signing Key. * &#x60;ZSK&#x60; - Zone Signing Key. | [optional] 
**privatekey** | **str** | The DS key&#39;s private key, in ISC format. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20095_result_data_additional_properties_keys_additional_properties import InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties from a JSON string
inline_response20095_result_data_additional_properties_keys_additional_properties_instance = InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties.to_json())

# convert the object into a dict
inline_response20095_result_data_additional_properties_keys_additional_properties_dict = inline_response20095_result_data_additional_properties_keys_additional_properties_instance.to_dict()
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties from a dict
inline_response20095_result_data_additional_properties_keys_additional_properties_from_dict = InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalProperties.from_dict(inline_response20095_result_data_additional_properties_keys_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



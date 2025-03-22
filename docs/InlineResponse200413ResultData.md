# InlineResponse200413ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cab** | **str** | The CA bundle&#39;s contents. | [optional] 
**created** | **int** | When the certificate was created. | [optional] 
**crt** | **str** | The certificate&#39;s contents in Base64 PEM format. | [optional] 
**domain_is_configured** | **int** | Whether the certificate is installed on the account. * &#x60;1&#x60; — Installed. * &#x60;0&#x60; — Not installed. | [optional] 
**domains** | **List[str]** | The domains that the CSR covers. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The certificate&#39;s friendly name. | [optional] 
**id** | **str** | The certificate&#39;s identification. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed. - &#x60;1&#x60; — Self-signed. - &#x60;0&#x60; — Not self-signed. | [optional] 
**issuer_common_name** | **str** | The name that issued the certificate. | [optional] 
**issuer_organization_name** | **str** | The certificate&#39;s organization. | [optional] 
**issuer_text** | **str** | The certificate&#39;s issuer information. | [optional] 
**key** | **str** | The private key in Base64 PEM format. | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | When the certificate expired. | [optional] 
**not_before** | **int** | When the certificate started. | [optional] 
**serial** | **str** | The certificate&#39;s serial number. | [optional] 
**signature_algorithm** | **str** | The OID of the hash algorithm used to sign the certificate request. | [optional] 
**subject_common_name** | **str** | The certificate&#39;s common name. | [optional] 
**subject_text** | **str** | The certificate&#39;s subject text information. | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type. * &#x60;ev&#x60; — Extended Validation. * &#x60;ov&#x60; — Organization Validated. * &#x60;dv&#x60; — Domain Validated. * &#x60;null&#x60; —  The system could not parse and determine the certificate&#39;s validation type. | [optional] 
**verify_error** | **str** | A message that explains the reason for a verification error. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200413_result_data import InlineResponse200413ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200413ResultData from a JSON string
inline_response200413_result_data_instance = InlineResponse200413ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200413ResultData.to_json())

# convert the object into a dict
inline_response200413_result_data_dict = inline_response200413_result_data_instance.to_dict()
# create an instance of InlineResponse200413ResultData from a dict
inline_response200413_result_data_from_dict = InlineResponse200413ResultData.from_dict(inline_response200413_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



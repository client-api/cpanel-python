# InlineResponse200426ResultCertificate

An object that contains information about each certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_ssl_provider** | **str** | The AutoSSL provider&#39;s name. | [optional] 
**auto_ssl_provider_display_name** | **str** | The AutoSSL provider&#39;s display name. | [optional] 
**domains** | **List[str]** | The domains that the certificate covers. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**is_autossl** | **int** | Whether the AutoSSL service provided the certificate. * &#x60;1&#x60; - Provided by the AutoSSL service. * &#x60;0&#x60; - Not provided by the AutoSSL service. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed. * &#x60;1&#x60; - Self-signed. * &#x60;0&#x60; - Not self-signed. | [optional] 
**issuer_common_name** | **str** | The name that issued the certificate. | [optional] 
**issuer_organization_name** | **str** | The certificate&#39;s organization name. | [optional] 
**issuer_text** | **str** | The issuer&#39;s X.509 information. | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The certificate&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | When the certificate expired. | [optional] 
**not_before** | **int** | When the certificate started. | [optional] 
**signature_algorithm** | **str** | The signature algorithm of the certificate. | [optional] 
**subject_common_name** | **str** | The certificate&#39;s common name. | [optional] 
**subject_text** | **str** | The subject&#39;s X.509 information. | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type.  **Note:** * &#x60;ev&#x60; -  Extended Validation. * &#x60;ov&#x60; - Organization Validation. * &#x60;dv&#x60; - Domain Validation. * null - The system could not parse and determine the certificate&#39;s validation type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200426_result_certificate import InlineResponse200426ResultCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200426ResultCertificate from a JSON string
inline_response200426_result_certificate_instance = InlineResponse200426ResultCertificate.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200426ResultCertificate.to_json())

# convert the object into a dict
inline_response200426_result_certificate_dict = inline_response200426_result_certificate_instance.to_dict()
# create an instance of InlineResponse200426ResultCertificate from a dict
inline_response200426_result_certificate_from_dict = InlineResponse200426ResultCertificate.from_dict(inline_response200426_result_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



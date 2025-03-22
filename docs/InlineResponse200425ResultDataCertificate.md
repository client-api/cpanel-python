# InlineResponse200425ResultDataCertificate

An object containing the certificate information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The domains that the certificate covers. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed. * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — Not self-signed. | [optional] 
**issuer_common_name** | **str** | The issuer&#39;s Common Name, typically a domain name. | [optional] 
**issuer_organization_name** | **str** | The certificate&#39;s organization. | [optional] 
**issuer_text** | **str** | The X.509 information about the issuer that contains CSR information. | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.    * &#x60;rsaEncryption&#x60; — RSA.   * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The certificate&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | The certificate&#39;s expiration time. | [optional] 
**not_before** | **int** | The certificate&#39;s start time. | [optional] 
**signature_algorithm** | **str** | The signature algorithm of the certificate. | [optional] 
**subject_common_name** | **str** | The certificate&#39;s Common Name. | [optional] 
**subject_text** | **str** | The X.509 information about the certificate&#39;s subject that contains CSR information. | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type. * &#x60;ev&#x60; — Extended Validation. * &#x60;ov&#x60; — Organization Validation. * &#x60;dv&#x60; — Domain Validation. * &#x60;null&#x60; — The system could not parse and determine the certificate&#39;s validation type. | [optional] 
**verify_error** | **str** | Any errors that exist during the certificate verification process. If there are no errors, this will return an empty string.  **Note:**  You **must** set the &#x60;verify_certificate&#x60; parameter to &#x60;1&#x60; for this return to appear. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200425_result_data_certificate import InlineResponse200425ResultDataCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200425ResultDataCertificate from a JSON string
inline_response200425_result_data_certificate_instance = InlineResponse200425ResultDataCertificate.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200425ResultDataCertificate.to_json())

# convert the object into a dict
inline_response200425_result_data_certificate_dict = inline_response200425_result_data_certificate_instance.to_dict()
# create an instance of InlineResponse200425ResultDataCertificate from a dict
inline_response200425_result_data_certificate_from_dict = InlineResponse200425ResultDataCertificate.from_dict(inline_response200425_result_data_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



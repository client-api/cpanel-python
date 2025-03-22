# InlineResponse200430ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | The date the certificate was created. | [optional] 
**domain_is_configured** | **int** | Whether the certificate is installed on the account.  * &#x60;1&#x60; — Installed. * &#x60;0&#x60; — Not installed. | [optional] 
**domains** | **List[str]** | A list of domains that the certificate covers. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The certificate&#39;s friendly name. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed.  * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — Not self-signed. | [optional] 
**issuer_common_name** | **str** | The issuer&#39;s name. | [optional] 
**issuer_organization_name** | **str** | The certificate&#39;s organization. | [optional] 
**issuer_text** | **str** | The certificate&#39;s issuer information. | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The certificate&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | The certificate&#39;s expiration date. | [optional] 
**not_before** | **int** | The certificate&#39;s start date. | [optional] 
**serial** | **str** | The certificate&#39;s serial number. | [optional] 
**signature_algorithm** | **str** | The OID hash algorithm signature of the certificate. | [optional] 
**subject_common_name** | **str** | The certificate&#39;s Common Name (CN). | [optional] 
**subject_text** | **str** | The certificate&#39;s subject text information. | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type.  * &#x60;ev&#x60; — Extended Validation. * &#x60;ov&#x60; — Organization Validation. * &#x60;dv&#x60; — Domain Validation. * &#x60;null&#x60; — The system could not parse and determine the certificate&#39;s validation type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200430_result_data import InlineResponse200430ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200430ResultData from a JSON string
inline_response200430_result_data_instance = InlineResponse200430ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200430ResultData.to_json())

# convert the object into a dict
inline_response200430_result_data_dict = inline_response200430_result_data_instance.to_dict()
# create an instance of InlineResponse200430ResultData from a dict
inline_response200430_result_data_from_dict = InlineResponse200430ResultData.from_dict(inline_response200430_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



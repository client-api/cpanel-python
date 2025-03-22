# InlineResponse200449ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | The certificate&#39;s creation date. | [optional] 
**domains** | **List[str]** | A list of the certificate&#39;s domains. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The certificate&#39;s friendly name. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed.  * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — Not self-signed. | [optional] 
**issuer_common_name** | **str** | The issuer&#39;s Common Name or Distinguished Name. | [optional] 
**issuer_organization_name** | **str** | The issuer&#39;s Organization Name. | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The certificate&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the certificate&#39;s key&#39;s modulus.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | The certificate&#39;s expiration date. | [optional] 
**not_before** | **int** | The certificate&#39;s start date. | [optional] 
**signature_algorithm** | **str** | The certificiate&#39;s OID hash algorithm signature. | [optional] 
**subject_common_name** | **str** | The issuer&#39;s Common Name or Distinguished Name. | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type.  * &#x60;ev&#x60; — Extended Validation. * &#x60;ov&#x60; — Organization Validation. * &#x60;dv&#x60; — Domain Validation. * &#x60;null&#x60; — The system could not parse and determine the certificate&#39;s validation type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200449_result_data import InlineResponse200449ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200449ResultData from a JSON string
inline_response200449_result_data_instance = InlineResponse200449ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200449ResultData.to_json())

# convert the object into a dict
inline_response200449_result_data_dict = inline_response200449_result_data_instance.to_dict()
# create an instance of InlineResponse200449ResultData from a dict
inline_response200449_result_data_from_dict = InlineResponse200449ResultData.from_dict(inline_response200449_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



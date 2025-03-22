# InlineResponse200444ResultDataDetails

An object containing the certificate's details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | A list of the certificate&#39;s domains. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the certificate&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The certificate&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The certificate&#39;s friendly name. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed.  * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — Not self-signed. | [optional] 
**issuer** | [**InlineResponse200444ResultDataDetailsIssuer**](InlineResponse200444ResultDataDetailsIssuer.md) |  | [optional] 
**key_algorithm** | **str** | The certificate&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The certificate&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The certificate&#39;s key is **not** an RSA key. | [optional] 
**not_after** | **int** | The certificate&#39;s expiration date. | [optional] 
**not_before** | **int** | The certificate&#39;s start time. | [optional] 
**signature_algorithm** | **str** | The certificate&#39;s OID hash algorithm signature. | [optional] 
**subject** | [**InlineResponse200444ResultDataDetailsSubject**](InlineResponse200444ResultDataDetailsSubject.md) |  | [optional] 
**validation_type** | **str** | The certificate&#39;s validation type.  * &#x60;ev&#x60; — Extended Validation. * &#x60;ov&#x60; — Organization Validation. * &#x60;dv&#x60; — Domain Validation. * &#x60;null&#x60; — The system could not parse and determine the certificate&#39;s validation type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200444_result_data_details import InlineResponse200444ResultDataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200444ResultDataDetails from a JSON string
inline_response200444_result_data_details_instance = InlineResponse200444ResultDataDetails.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200444ResultDataDetails.to_json())

# convert the object into a dict
inline_response200444_result_data_details_dict = inline_response200444_result_data_details_instance.to_dict()
# create an instance of InlineResponse200444ResultDataDetails from a dict
inline_response200444_result_data_details_from_dict = InlineResponse200444ResultDataDetails.from_dict(inline_response200444_result_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



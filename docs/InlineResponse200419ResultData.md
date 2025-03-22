# InlineResponse200419ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | The key&#39;s creation date. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The key&#39;s friendly name. | [optional] 
**id** | **str** | The key&#39;s ID. | [optional] 
**key_algorithm** | **str** | The key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The key is **not** an RSA key. | [optional] 
**modulus_length** | **int** | The length, in bits, of the key&#39;s modulus.  * &#x60;null&#x60; — The key is **not** an RSA key. | [optional] 
**text** | **str** | The key&#39;s contents. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200419_result_data import InlineResponse200419ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200419ResultData from a JSON string
inline_response200419_result_data_instance = InlineResponse200419ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200419ResultData.to_json())

# convert the object into a dict
inline_response200419_result_data_dict = inline_response200419_result_data_instance.to_dict()
# create an instance of InlineResponse200419ResultData from a dict
inline_response200419_result_data_from_dict = InlineResponse200419ResultData.from_dict(inline_response200419_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



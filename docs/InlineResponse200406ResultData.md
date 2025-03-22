# InlineResponse200406ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The CSR&#39;s Common Name. | [optional] 
**created** | **int** | The CSR&#39;s creation date. | [optional] 
**domains** | **List[str]** | A list of the domains that the CSR covers. | [optional] 
**ecdsa_curve_name** | **str** | The ECDSA curve that the CSR&#39;s key uses.  * &#x60;prime256v1&#x60; * &#x60;secp384r1&#x60; * &#x60;null&#x60; — The CSR&#39;s key is **not** an ECDSA key. | [optional] 
**ecdsa_public** | **str** | The CSR&#39;s key&#39;s ECDSA compressed public point, in hexadecimal format.  * &#x60;null&#x60; — The CSR&#39;s key is **not** an ECDSA key. | [optional] 
**friendly_name** | **str** | The CSR&#39;s friendly name. | [optional] 
**id** | **str** | The CSR&#39;s ID. | [optional] 
**key_algorithm** | **str** | The CSR&#39;s key&#39;s algorithm.  * &#x60;rsaEncryption&#x60; — RSA. * &#x60;id-ecPublicKey&#x60; — ECDSA. | [optional] 
**modulus** | **str** | The CSR&#39;s key&#39;s modulus, in hexadecimal format.  * &#x60;null&#x60; — The CSR&#39;s key is **not** an RSA key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200406_result_data import InlineResponse200406ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200406ResultData from a JSON string
inline_response200406_result_data_instance = InlineResponse200406ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200406ResultData.to_json())

# convert the object into a dict
inline_response200406_result_data_dict = inline_response200406_result_data_instance.to_dict()
# create an instance of InlineResponse200406ResultData from a dict
inline_response200406_result_data_from_dict = InlineResponse200406ResultData.from_dict(inline_response200406_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



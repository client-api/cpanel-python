# InlineResponse200307ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **int** | When the system placed the order. | [optional] 
**csr** | **str** | The certificate signing request&#39;s (CSR) text. A CSR file in Base64 PEM format. | [optional] 
**domains** | **List[str]** | The domains on the certificate. | [optional] 
**expired** | **int** | Whether the pending queue item has been deleted. * &#x60;1&#x60; - Deleted. * &#x60;0&#x60; - **Not** deleted. | [optional] 
**first_poll_time** | **int** | The first time that the system polled the provider for the certificate. | [optional] 
**identity_verification** | **object** | hash that contains information to verify an OV or EV certificate request.  **Notes:**   The function returns this hash for OV or EV certificate requests. This hash includes returns that vary between certificate providers. The output example demonstrates what the cPStore returns for an OV certificate. | [optional] 
**last_poll_time** | **int** | The last time that the system polled the provider for the certificate. | [optional] 
**last_status_code** | **str** | The last status code of the order. The function returns the value in the unnamed hash. * &#x60;CertificateNotFound&#x60; - The system cannot locate the specified certificate. * &#x60;RequiresApproval&#x60; - The specified certificate requires approval. * &#x60;OrderCanceled&#x60; - The system canceled the order of the specified certificate. * &#x60;OrderItemCanceled&#x60; - The system canceled the order item of the specified certificate. | [optional] 
**order_id** | **str** | The ID of the order. | [optional] 
**order_item_id** | **str** | The ID of the ordered item. | [optional] 
**product_id** | **str** | The product&#39;s ID. | [optional] 
**provider** | **str** | The cPanel Market provider&#39;s name. | [optional] 
**status** | **str** | The status of the order. * &#x60;confirmed&#x60; - Payment confirmed. * &#x60;unconfirmed&#x60; - Payment not confirmed. | [optional] 
**support_uri** | **str** | The URI of the cPanel Market Provider&#39;s support site. | [optional] 
**vhost_names** | **List[str]** | The virtual host domains on the certificate. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200307_result_data import InlineResponse200307ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200307ResultData from a JSON string
inline_response200307_result_data_instance = InlineResponse200307ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200307ResultData.to_json())

# convert the object into a dict
inline_response200307_result_data_dict = inline_response200307_result_data_instance.to_dict()
# create an instance of InlineResponse200307ResultData from a dict
inline_response200307_result_data_from_dict = InlineResponse200307ResultData.from_dict(inline_response200307_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200311ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_pem** | **str** | The text of the certificate, if available. * &#x60;null&#x60; - The certificate is not available. | [optional] 
**created_time** | **int** | When the system placed the order. | [optional] 
**csr** | **str** | The Certificate Signing Request&#39;s (CSR&#39;s) text. | [optional] 
**deleted** | **int** | Whether the system has deleted the item from the pending queue. * &#x60;0&#x60; - Deleted. * &#x60;1&#x60; - **Not** deleted. | [optional] 
**domains** | **List[str]** | A list of domains that the certificate request covers. | [optional] 
**expired** | **int** | Whether the system has deleted the item from the pending queue. * &#x60;1&#x60; - Deleted. * &#x60;0&#x60; - **Not** deleted. | [optional] 
**first_poll_time** | **int** | The first time that the system polled the provider for the certificate. | [optional] 
**installed** | **int** | Whether the system installed the certificate. * &#x60;1&#x60; - Installed. * &#x60;0&#x60; - **Not** installed. | [optional] 
**last_poll_time** | **int** | The last time that the system polled the provider for the certificate. | [optional] 
**last_status_code** | **str** | The last status code of the order. * &#x60;CertificateNotFound&#x60; - The system cannot locate the specified certificate. * &#x60;RequiresApproval&#x60; - The specified certificate requires approval. * &#x60;OrderCanceled&#x60; - The system canceled the order of the specified certificate. * &#x60;OrderItemCanceled&#x60; - The system canceled the order item of the specified certificate. | [optional] 
**last_status_message** | **str** | An error message from the certificate provider. For example, why a certificate authority rejected an SSL certificate.  **Note:**  If no error message exists, this will return an empty string. | [optional] 
**order_id** | **str** | A unique identifier for the order. | [optional] 
**order_item_id** | **str** | A unique identifier of each item in the order. | [optional] 
**product_id** | **str** | An identifier for a given product. | [optional] 
**provider** | **str** | The cPanel Market provider&#39;s name. | [optional] 
**status** | **str** | The status of the order. * &#x60;confirmed&#x60; - Payment confirmed. * &#x60;unconfirmed&#x60; - Payment **not** confirmed. | [optional] 
**vhost_names** | **List[str]** | A list of virtual host names. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200311_result_data import InlineResponse200311ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200311ResultData from a JSON string
inline_response200311_result_data_instance = InlineResponse200311ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200311ResultData.to_json())

# convert the object into a dict
inline_response200311_result_data_dict = inline_response200311_result_data_instance.to_dict()
# create an instance of InlineResponse200311ResultData from a dict
inline_response200311_result_data_from_dict = InlineResponse200311ResultData.from_dict(inline_response200311_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



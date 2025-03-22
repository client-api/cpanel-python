# InlineResponse200305ResultDataStatusDetails

An object that contains specific information about the validation process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_val_status** | **str** | Whether the brand validation status has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The certificate&#39;s brand validation is **not** complete. * &#x60;completed&#x60; - The certificate&#39;s brand validation is complete. * &#x60;in-progress&#x60; - The certificate&#39;s brand validation is in progress. | [optional] 
**certificate_status** | **str** | Whether the provider has issued the SSL certificate.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The certificate&#39;s issue is **not** completed. * &#x60;completed&#x60; - The provider has issued the certificate. * &#x60;in-progress&#x60; - The certificate&#39;s issue is in progress. | [optional] 
**csr_status** | **str** | Whether the certificate signing request (CSR) has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The CSR for the certificate is **not** complete. * &#x60;completed&#x60; - The CSR for the certificate is complete. * &#x60;in-progress&#x60; - The CSR for the certificate is in progress. | [optional] 
**dcv_status** | **str** | Whether Domain Control Validation (DCV) has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The DCV for the certificate is **not** complete. * &#x60;completed&#x60; - The DCV for the certificate is complete. * &#x60;in-progress&#x60; - The DCV for the certificate is in progress. | [optional] 
**ev_click_through_status** | **str** | Whether every requirement for the EV certificate has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The EV certificate&#39;s requirements check is **not** complete. * &#x60;completed&#x60; - The EV certificate&#39;s requirements check is complete. * &#x60;in-progress&#x60; - The EV certificate&#39;s requirements check is in progress.  For more information, read Sectigo&#39;s [What is required for validation?](https://support.sectigo.com/Com_KnowledgeDetailPage?Id&#x3D;kA01N000000zFOr) documentation. | [optional] 
**free_dvup_status** | **str** | Whether every requirement for the Domain Validated (DV) certificate has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The DV certificate&#39;s requirements check is **not** complete. * &#x60;completed&#x60; - The DV certificate&#39;s requirements check is complete. * &#x60;in-progress&#x60; - The DV certificate&#39;s requirements check is in progress. | [optional] 
**organization_validation_status** | **str** | Whether every requirement for the OV certificate has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The OV certificate&#39;s requirements check is **not** complete. * &#x60;completed&#x60; - The OV certificate&#39;s requirements check is complete. * &#x60;in-progress&#x60; - The OV certificate&#39;s requirements check is in progress. | [optional] 
**ov_callback_status** | **str** | Whether the Certificate Authority (CA) has verified the organization&#39;s validity via a phone call.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The CA has **not** verified the organization&#39;s validity via phone. * &#x60;completed&#x60; - The CA has verified the organization&#39;s validity via phone. * &#x60;in-progress&#x60; - The CA&#39;s verification of the organization&#39;s validity via phone is in progress. | [optional] 
**validation_status** | **str** | Whether the validation process has completed.  * &#x60;not applicable&#x60; - This is **not** applicable for the certificate. * &#x60;not-completed&#x60; - The certificate&#39;s validation is **not** complete. * &#x60;completed&#x60; - The certificate&#39;s validation is complete. * &#x60;in-progress&#x60; - The certificate&#39;s validation is in progress. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200305_result_data_status_details import InlineResponse200305ResultDataStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200305ResultDataStatusDetails from a JSON string
inline_response200305_result_data_status_details_instance = InlineResponse200305ResultDataStatusDetails.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200305ResultDataStatusDetails.to_json())

# convert the object into a dict
inline_response200305_result_data_status_details_dict = inline_response200305_result_data_status_details_instance.to_dict()
# create an instance of InlineResponse200305ResultDataStatusDetails from a dict
inline_response200305_result_data_status_details_from_dict = InlineResponse200305ResultDataStatusDetails.from_dict(inline_response200305_result_data_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



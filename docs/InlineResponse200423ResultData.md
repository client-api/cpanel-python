# InlineResponse200423ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_match_method** | **str** | The method that the system used to match the certificate with the mail service.  * &#x60;none&#x60; — No domain matches the certificate. * &#x60;exact&#x60; — The domain exactly matches the certificate. * &#x60;exact-wildcard&#x60; — The domain exactly matches the certificate. * &#x60;mail-wildcard&#x60; — The &#x60;mail&#x60; subdomain of the domain matches the domain of the wildcard certificate. * &#x60;www-wildcard&#x60; — The &#x60;www&#x60; subdomain of the domain matches the domain of the wildcard certificate. * &#x60;hostname-wildcard&#x60; — The hostname&#39;s domain matches the domain of the wildcard certificate. * &#x60;hostname&#x60; — The hostname matches the domain of the certificate. * &#x60;localdomain_on_cert-mail-wildcard&#x60; — A &#x60;mail&#x60; subdomain of a domain on the server that matches the certificate. * &#x60;localdomain_on_cert-www-wildcard&#x60; — A &#x60;www&#x60; subdomain of a domain on the server matches the certificate. * &#x60;localdomain_on_cert&#x60; — A domain on the server matches the certificate. | [optional] 
**cert_valid_not_after** | **int** | The certificate&#39;s expiration date. | [optional] 
**is_currently_valid** | **int** | Whether the certificate is currently valid.  * &#x60;1&#x60; — Valid. * &#x60;0&#x60; — Invalid.  **Note:**  If the certificate is valid, the following statements are true:   * The certificate is **not** self-signed (the &#x60;ssldomain_matches_cert&#x60; value is &#x60;1&#x60;).   * The certificate matches the SSL domain (the &#x60;ssldomain_matches_cert&#x60; value is &#x60;1&#x60;).   * The certificate is within its validity period (the &#x60;cert_valid_not_after&#x60; value is **less** than the current time and date). | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed.  * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — Not self-signed.  **Note:**  If the &#x60;cert_match_method&#x60; value is &#x60;none&#x60;, you should ignore this return&#39;s value. | [optional] 
**is_wild_card** | **int** | Whether the certificate is a wildcard certificate.  * &#x60;1&#x60; — Wildcard. * &#x60;0&#x60; — Not a wildcard. | [optional] 
**ssldomain** | **str** | The best domain to use to access the service. | [optional] 
**ssldomain_matches_cert** | **int** | Whether an SSL-protected domain matches the certificate.  * &#x60;1&#x60; — Matches. * &#x60;0&#x60; — Does **not** match. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200423_result_data import InlineResponse200423ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200423ResultData from a JSON string
inline_response200423_result_data_instance = InlineResponse200423ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200423ResultData.to_json())

# convert the object into a dict
inline_response200423_result_data_dict = inline_response200423_result_data_instance.to_dict()
# create an instance of InlineResponse200423ResultData from a dict
inline_response200423_result_data_from_dict = InlineResponse200423ResultData.from_dict(inline_response200423_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



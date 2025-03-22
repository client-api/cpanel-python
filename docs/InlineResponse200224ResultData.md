# InlineResponse200224ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The target domain of the DMARC policy. | [optional] 
**error** | **str** | A message that details either why the DNS lookup failed, or if there is a SPF/DKIM failure.  **Note:**  This will be set to &#x60;MALFORMED&#x60; if there is a syntax issue with this domain&#39;s SPF and DKIM records. | [optional] 
**record** | **str** | The domain&#39;s DMARC TXT record. | [optional] 
**state** | **str** | The domain&#39;s DMARC record status. Possible values:  * &#x60;VALID&#x60; - A DMARC policy is set for the domain, along with valid SPF and DKIM records for the domain and IP address. * &#x60;MALFORMED&#x60; - A DMARC record is set, but it did not pass a syntax check. * &#x60;DKIM_SPF_ERROR&#x60; - A DMARC record exists; however, both the DKIM and SPF records for this domain did not pass validation. * &#x60;DKIM_ERROR&#x60; - A DMARC record exists; however, the DKIM record for this domain did not pass validation. * &#x60;SPF_ERROR&#x60; - A DMARC record exists; however, the SPF record for this domain did not pass validation. * &#x60;MISSING&#x60; - No DMARC record exists for the domain at the DMARC subdomain location. * &#x60;DNS_ERROR&#x60; - A DNS error prevented validation of the DMARC record. | [optional] 
**subdomain** | **str** | The domain that the function used to check the DMARC record. This will be the value of the &#x60;domain&#x60; parameter with a &#x60;_dmarc&#x60; prefix. | [optional] 
**suggested** | **str** | The recommended DMARC policy. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200224_result_data import InlineResponse200224ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200224ResultData from a JSON string
inline_response200224_result_data_instance = InlineResponse200224ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200224ResultData.to_json())

# convert the object into a dict
inline_response200224_result_data_dict = inline_response200224_result_data_instance.to_dict()
# create an instance of InlineResponse200224ResultData from a dict
inline_response200224_result_data_from_dict = InlineResponse200224ResultData.from_dict(inline_response200224_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



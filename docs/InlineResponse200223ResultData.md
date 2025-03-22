# InlineResponse200223ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the function used to check the DKIM record. This will be the value of the domain parameter with a &#x60;default._domainkey&#x60; prefix. | [optional] 
**error** | **str** | A message that details the reason why the DNS lookup failed.  **Note:**  The function only returns this value when the &#x60;state&#x60; returned is the &#x60;ERROR&#x60; value. | [optional] 
**expected** | **str** | The DKIM record&#39;s contents. | [optional] 
**records** | [**List[InlineResponse200223ResultRecords]**](InlineResponse200223ResultRecords.md) | The domain&#39;s DNS DKIM TXT records.  **Important:**  This function may fail to preserve whitespace in DKIM records. | [optional] 
**state** | **str** | The domain&#39;s DKIM record status. Possible values:  * &#x60;VALID&#x60; The DKIM record is valid. * &#x60;MALFORMED&#x60; A single DKIM record exists, but the record does not match the expected DKIM specifications. * &#x60;MISMATCH&#x60; A DKIM record exists, but it does not match the expected public key. * &#x60;MISSING&#x60; No DKIM record exists for the domain. * &#x60;MULTIPLE&#x60; Multiple DKIM records exist. * &#x60;NOPUB&#x60; No key exists on the local server for the domain. * &#x60;ERROR&#x60; The record&#39;s DNS lookup failed. The function returns the reason in the error return. | [optional] 
**validity_cache_update** | **str** | The result of the DKIM record&#39;s validity cache update operation: * &#x60;set&#x60; The domain is invalid but passed its validity check. The validity check now passes the domain as valid. * &#x60;unset&#x60; The domain is invalid and did not pass its validity check. The validity check does not pass the domain as valid. * &#x60;valid&#x60; The domain is valid and passed its validity check. There are no changes required. * &#x60;invalid&#x60; The domain is invalid and failed its validity check. There are no changes required. * &#x60;none&#x60; The domain is invalid, but the system will not take further action. * &#x60;error&#x60; The domain&#39;s validity check operation failed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200223_result_data import InlineResponse200223ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200223ResultData from a JSON string
inline_response200223_result_data_instance = InlineResponse200223ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200223ResultData.to_json())

# convert the object into a dict
inline_response200223_result_data_dict = inline_response200223_result_data_instance.to_dict()
# create an instance of InlineResponse200223ResultData from a dict
inline_response200223_result_data_from_dict = InlineResponse200223ResultData.from_dict(inline_response200223_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



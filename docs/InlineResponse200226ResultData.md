# InlineResponse200226ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The queried domain. | [optional] 
**error** | **str** | A message that details the reason why the DNS lookup failed.  **Note:**   The function **only** returns this value when the &#x60;state&#x60; return is the &#x60;ERROR&#x60; value. | [optional] 
**expected** | **str** | The SPF record for the domain in the DNS. | [optional] 
**ip_address** | **str** | The domain&#39;s IP address. | [optional] 
**ip_version** | **int** | The IP address version. * &#x60;4&#x60; * &#x60;6&#x60; | [optional] 
**records** | [**List[InlineResponse200226ResultRecords]**](InlineResponse200226ResultRecords.md) | The SPF records of the domain&#39;s DNS. | [optional] 
**state** | **str** | The SPF record&#39;s status: * &#x60;VALID&#x60; - A single &#x60;SPF TXT&#x60; record exists in the domain&#39;s DNS with the correct &#x60;ip_address&#x60; value or redirect mechanism. * &#x60;MISMATCHED&#x60; - An &#x60;SPF TXT&#x60; record exists for the domain that does **not** match the &#x60;ip_address&#x60; value. * &#x60;MULTIPLE&#x60; - Multiple &#x60;SPF TXT&#x60; records exist in the domain&#39;s DNS. * &#x60;MISSING&#x60; - No &#x60;SPF TXT&#x60; record exists for the domain&#39;s DNS. * &#x60;ERROR&#x60; - The record&#39;s DNS lookup failed. The function returns the reason in the error return. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200226_result_data import InlineResponse200226ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200226ResultData from a JSON string
inline_response200226_result_data_instance = InlineResponse200226ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200226ResultData.to_json())

# convert the object into a dict
inline_response200226_result_data_dict = inline_response200226_result_data_instance.to_dict()
# create an instance of InlineResponse200226ResultData from a dict
inline_response200226_result_data_from_dict = InlineResponse200226ResultData.from_dict(inline_response200226_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



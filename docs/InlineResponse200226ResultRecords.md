# InlineResponse200226ResultRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **str** | The SPF record&#39;s contents. | [optional] 
**reason** | **str** | The reason why the SPF record is **not** correct, if one exists.  **Note:**  If no errors exist, the function does **not** return this value. | [optional] 
**state** | **str** | The SPF record&#39;s status: * &#x60;PASS&#x60; - The &#x60;SPF&#x60; record confirms that the &#x60;ip_address&#x60; value is a valid sender. * &#x60;NEUTRAL&#x60; - The current &#x60;SPF&#x60; record configuration does not determine the &#x60;ip_address&#x60; value&#39;s validity. * &#x60;FAIL&#x60; - The &#x60;SPF&#x60; record states that the &#x60;ip_address&#x60; value is **not** a valid sender. * &#x60;SOFTFAIL&#x60; - The &#x60;SPF&#x60; record states that the &#x60;ip_address&#x60; value is **not** a valid sender, but does not &#x60;FAIL&#x60; state it. * &#x60;TEMPERROR&#x60; - The &#x60;SPF&#x60; record check resulted in a failure. For example, a network failure. * &#x60;PERMERROR&#x60; - The domain&#39;s &#x60;SPF&#x60; records are **incorrect** and require manual correction.  **Note:**  These values correspond with [RFC7208 section 2.6](https://tools.ietf.org/html/rfc7208#section-2.6). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200226_result_records import InlineResponse200226ResultRecords

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200226ResultRecords from a JSON string
inline_response200226_result_records_instance = InlineResponse200226ResultRecords.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200226ResultRecords.to_json())

# convert the object into a dict
inline_response200226_result_records_dict = inline_response200226_result_records_instance.to_dict()
# create an instance of InlineResponse200226ResultRecords from a dict
inline_response200226_result_records_from_dict = InlineResponse200226ResultRecords.from_dict(inline_response200226_result_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



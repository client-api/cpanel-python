# InlineResponse200223ResultRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **str** | The domain&#39;s DKIM TXT record data contents.  **Important:**   This function may fail to preserve whitespace in DKIM records. | [optional] 
**reason** | **str** | The reason why the DKIM TXT record is not correct, if one exists.  **Note:**  This function **only** returns this value when the &#x60;state&#x60; value is &#x60;PERMFAIL&#x60;. | [optional] 
**state** | **str** | The DKIM TXT record&#39;s status: * &#x60;VALID&#x60; - The DKIM TXT record matches the local server&#39;s public key. * &#x60;MISMATCH&#x60; - The DKIM TXT record does not match the local server&#39;s public key. * &#x60;PERMFAIL&#x60; - Multiple DKIM TXT records for the domain exist or a misconfigured DKIM TXT record exists. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200223_result_records import InlineResponse200223ResultRecords

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200223ResultRecords from a JSON string
inline_response200223_result_records_instance = InlineResponse200223ResultRecords.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200223ResultRecords.to_json())

# convert the object into a dict
inline_response200223_result_records_dict = inline_response200223_result_records_instance.to_dict()
# create an instance of InlineResponse200223ResultRecords from a dict
inline_response200223_result_records_from_dict = InlineResponse200223ResultRecords.from_dict(inline_response200223_result_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



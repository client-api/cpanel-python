# InlineResponse200312ResultDataCertificates

Information about each certificate in the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The private key&#39;s ID. | [optional] 
**order_item_id** | **int** | The ID of the ordered item. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200312_result_data_certificates import InlineResponse200312ResultDataCertificates

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200312ResultDataCertificates from a JSON string
inline_response200312_result_data_certificates_instance = InlineResponse200312ResultDataCertificates.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200312ResultDataCertificates.to_json())

# convert the object into a dict
inline_response200312_result_data_certificates_dict = inline_response200312_result_data_certificates_instance.to_dict()
# create an instance of InlineResponse200312ResultDataCertificates from a dict
inline_response200312_result_data_certificates_from_dict = InlineResponse200312ResultDataCertificates.from_dict(inline_response200312_result_data_certificates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



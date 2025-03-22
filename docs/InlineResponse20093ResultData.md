# InlineResponse20093ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnskey** | **str** | The DNSKEY record value. | [optional] 
**key_id** | **int** | The DNSSEC record&#39;s ID. | [optional] 
**success** | **int** | Whether the DNSKEY record exported successfully.  * &#x60;1&#x60; - The system exported the record successfully. * &#x60;0&#x60; - The system failed to export the record. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20093_result_data import InlineResponse20093ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20093ResultData from a JSON string
inline_response20093_result_data_instance = InlineResponse20093ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20093ResultData.to_json())

# convert the object into a dict
inline_response20093_result_data_dict = inline_response20093_result_data_instance.to_dict()
# create an instance of InlineResponse20093ResultData from a dict
inline_response20093_result_data_from_dict = InlineResponse20093ResultData.from_dict(inline_response20093_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



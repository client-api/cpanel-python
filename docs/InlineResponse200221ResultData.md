# InlineResponse200221ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The SPF record&#39;s associated domain on the DNS server. | [optional] 
**msg** | **str** | The SPF record&#39;s installation status to the DNS server. | [optional] 
**status** | **int** | Whether the system installed the SPF record to the DNS server. - &#x60;1&#x60; - The system installed the SPF record on the DNS server. - &#x60;0&#x60; - The system **cannot** install the SPF record on the DNS server. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200221_result_data import InlineResponse200221ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200221ResultData from a JSON string
inline_response200221_result_data_instance = InlineResponse200221ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200221ResultData.to_json())

# convert the object into a dict
inline_response200221_result_data_dict = inline_response200221_result_data_instance.to_dict()
# create an instance of InlineResponse200221ResultData from a dict
inline_response200221_result_data_from_dict = InlineResponse200221ResultData.from_dict(inline_response200221_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



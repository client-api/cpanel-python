# InlineResponse200561ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** | The unique ID of the backup process. | [optional] 
**site** | **str** | The WordPress site&#39;s URL without the protocol prefix. | [optional] 
**sse_url** | **str** | The SSE path **without** the protocol, hostname, or port that the system uses to monitor the backup progress. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200561_result_data import InlineResponse200561ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200561ResultData from a JSON string
inline_response200561_result_data_instance = InlineResponse200561ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200561ResultData.to_json())

# convert the object into a dict
inline_response200561_result_data_dict = inline_response200561_result_data_instance.to_dict()
# create an instance of InlineResponse200561ResultData from a dict
inline_response200561_result_data_from_dict = InlineResponse200561ResultData.from_dict(inline_response200561_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



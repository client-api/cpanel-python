# InlineResponse200548ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_id** | **int** | The deployment ID number. | [optional] 
**log_path** | **str** | The absolute path to the task&#39;s log file. | [optional] 
**repository_root** | **str** | The aboslute path to the cPanel-managed repository directory. | [optional] 
**repository_state** | [**InlineResponse200548ResultRepositoryState**](InlineResponse200548ResultRepositoryState.md) |  | [optional] 
**sse_url** | **str** | The SSE interface to track the progress of the deployment process. | [optional] 
**task_id** | **str** | The [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) system&#39;s task ID number. | [optional] 
**timestamps** | [**InlineResponse200548ResultTimestamps**](InlineResponse200548ResultTimestamps.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200548_result_data import InlineResponse200548ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200548ResultData from a JSON string
inline_response200548_result_data_instance = InlineResponse200548ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200548ResultData.to_json())

# convert the object into a dict
inline_response200548_result_data_dict = inline_response200548_result_data_instance.to_dict()
# create an instance of InlineResponse200548ResultData from a dict
inline_response200548_result_data_from_dict = InlineResponse200548ResultData.from_dict(inline_response200548_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200542ResultDataTasks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The task&#39;s action.  * &#x60;create&#x60;  **Note:**  &#x60;create&#x60; is the only possible value. | [optional] 
**args** | [**InlineResponse200542ResultDataArgs**](InlineResponse200542ResultDataArgs.md) |  | [optional] 
**id** | **str** | The [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) system&#39;s task ID number. | [optional] 
**sse_url** | **str** | The SSE interface to track the progress of the process. | [optional] 
**subsystem** | **str** | The [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) subsystem that will handle the task.  * &#x60;VersionControl&#x60;  **Note:**  &#x60;VersionControl&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200542_result_data_tasks import InlineResponse200542ResultDataTasks

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200542ResultDataTasks from a JSON string
inline_response200542_result_data_tasks_instance = InlineResponse200542ResultDataTasks.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200542ResultDataTasks.to_json())

# convert the object into a dict
inline_response200542_result_data_tasks_dict = inline_response200542_result_data_tasks_instance.to_dict()
# create an instance of InlineResponse200542ResultDataTasks from a dict
inline_response200542_result_data_tasks_from_dict = InlineResponse200542ResultDataTasks.from_dict(inline_response200542_result_data_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



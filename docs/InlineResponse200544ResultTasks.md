# InlineResponse200544ResultTasks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The task&#39;s action.  * &#x60;create&#x60; — Create the repository. * &#x60;deploy&#x60; — Deploy the repository. | [optional] 
**args** | [**InlineResponse200544ResultArgs**](InlineResponse200544ResultArgs.md) |  | [optional] 
**id** | **str** | The Task Queue system&#39;s task ID number. | [optional] 
**sse_url** | **str** | The Secure Server Events (SSE) interface URL to track the progress of the process. | [optional] 
**subsystem** | **str** | The Task Queue subsystem that will handle the task.  * &#x60;VersionControl&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200544_result_tasks import InlineResponse200544ResultTasks

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200544ResultTasks from a JSON string
inline_response200544_result_tasks_instance = InlineResponse200544ResultTasks.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200544ResultTasks.to_json())

# convert the object into a dict
inline_response200544_result_tasks_dict = inline_response200544_result_tasks_instance.to_dict()
# create an instance of InlineResponse200544ResultTasks from a dict
inline_response200544_result_tasks_from_dict = InlineResponse200544ResultTasks.from_dict(inline_response200544_result_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



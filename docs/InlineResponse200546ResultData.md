# InlineResponse200546ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_id** | **str** | The deployment ID number. | [optional] 
**log_path** | **str** | The absolute path to the task&#39;s log file vc_TIMESTAMP_git_deploy.log, where TIMESTAMP represents the time in Unix epoch time. | [optional] 
**repository_root** | **str** | The repository&#39;s directory. | [optional] 
**sse_url** | **str** | The SSE interface to track the progress of the deployment process. | [optional] 
**task_id** | **str** | The Task Queue system&#39;s task ID number. | [optional] 
**timestamps** | [**InlineResponse200546ResultDataTimestamps**](InlineResponse200546ResultDataTimestamps.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200546_result_data import InlineResponse200546ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200546ResultData from a JSON string
inline_response200546_result_data_instance = InlineResponse200546ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200546ResultData.to_json())

# convert the object into a dict
inline_response200546_result_data_dict = inline_response200546_result_data_instance.to_dict()
# create an instance of InlineResponse200546ResultData from a dict
inline_response200546_result_data_from_dict = InlineResponse200546ResultData.from_dict(inline_response200546_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



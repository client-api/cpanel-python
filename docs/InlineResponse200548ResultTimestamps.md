# InlineResponse200548ResultTimestamps

An object containing timestamps for the deployment process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | The time at which the system started the deployment process, in Unix time format. | [optional] 
**canceled** | **str** | The time at which the system cancelled the deployment process, in Unix time format.  **Note:**  * The function only returns this value if the system cancelled the deployment process. * The system logs messages for this function in the &#x60;~/.cpanel/logs/vc_TIMESTAMP_git_deploy.log&#x60; file, where &#x60;TIMESTAMP&#x60; represents the Unix timestamp. | [optional] 
**failed** | **str** | The time at which the deployment process failed, in Unix time format.  **Note:**  * The function only returns this value if the deployment process failed. * The system logs messages for this function in the &#x60;~/.cpanel/logs/vc_TIMESTAMP_git_deploy.log&#x60; file, where &#x60;TIMESTAMP&#x60; represents the Unix timestamp. | [optional] 
**queued** | **str** | The time at which the deployment process entered the task queue, in Unix time format. | [optional] 
**succeeded** | **str** | The time at which the deployment process finished successfully, in Unix time format.  **Note:**   The function only returns this value if the deployment process succeeded. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200548_result_timestamps import InlineResponse200548ResultTimestamps

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200548ResultTimestamps from a JSON string
inline_response200548_result_timestamps_instance = InlineResponse200548ResultTimestamps.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200548ResultTimestamps.to_json())

# convert the object into a dict
inline_response200548_result_timestamps_dict = inline_response200548_result_timestamps_instance.to_dict()
# create an instance of InlineResponse200548ResultTimestamps from a dict
inline_response200548_result_timestamps_from_dict = InlineResponse200548ResultTimestamps.from_dict(inline_response200548_result_timestamps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



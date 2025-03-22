# InlineResponse200542ResultDataArgs

A list of arguments for the [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) system's process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_file** | **str** | The absolute path to the process&#39;s log file.  **Note:**  The function **only** returns this value if the process generated a log file. | [optional] 
**repository_root** | **str** | The absolute path to the repository&#39;s directory within the user&#39;s &#x60;home&#x60; directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200542_result_data_args import InlineResponse200542ResultDataArgs

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200542ResultDataArgs from a JSON string
inline_response200542_result_data_args_instance = InlineResponse200542ResultDataArgs.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200542ResultDataArgs.to_json())

# convert the object into a dict
inline_response200542_result_data_args_dict = inline_response200542_result_data_args_instance.to_dict()
# create an instance of InlineResponse200542ResultDataArgs from a dict
inline_response200542_result_data_args_from_dict = InlineResponse200542ResultDataArgs.from_dict(inline_response200542_result_data_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



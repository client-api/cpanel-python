# InlineResponse200544ResultArgs

A list of arguments for the Task Queue system's process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_file** | **str** | The absolute path to the process&#39;s log file.  **Note:**  The function only returns this value if the process generated a log file. | [optional] 
**repository_root** | **str** | The absolute path to the repository&#39;s directory in the user&#39;s &#x60;home&#x60; directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200544_result_args import InlineResponse200544ResultArgs

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200544ResultArgs from a JSON string
inline_response200544_result_args_instance = InlineResponse200544ResultArgs.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200544ResultArgs.to_json())

# convert the object into a dict
inline_response200544_result_args_dict = inline_response200544_result_args_instance.to_dict()
# create an instance of InlineResponse200544ResultArgs from a dict
inline_response200544_result_args_from_dict = InlineResponse200544ResultArgs.from_dict(inline_response200544_result_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



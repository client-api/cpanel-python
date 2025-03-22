# InlineResponse200545ResultDataArgs

An object containing arguments for the Task Queue system's process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_file** | **str** | The absolute path to the process log file in the user&#39;s &#x60;home&#x60; directory.  **Note:**  The function **only** returns this value if the process generated a log file. | [optional] 
**repository_root** | **str** | The repository&#39;s absolute directory path in the user&#39;s &#x60;home&#x60; directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200545_result_data_args import InlineResponse200545ResultDataArgs

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200545ResultDataArgs from a JSON string
inline_response200545_result_data_args_instance = InlineResponse200545ResultDataArgs.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200545ResultDataArgs.to_json())

# convert the object into a dict
inline_response200545_result_data_args_dict = inline_response200545_result_data_args_instance.to_dict()
# create an instance of InlineResponse200545ResultDataArgs from a dict
inline_response200545_result_data_args_from_dict = InlineResponse200545ResultDataArgs.from_dict(inline_response200545_result_data_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



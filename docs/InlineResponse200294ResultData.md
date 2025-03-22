# InlineResponse200294ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_logs** | **int** | Whether the system archives log files to your home directory. * &#x60;1&#x60; — Archives the logs. * &#x60;0&#x60; — Does **not** archive the logs. | [optional] 
**prune_archive** | **int** | Whether the system removes the previous month&#39;s archived log files from your home directory. * &#x60;1&#x60; — Removes the logs. * &#x60;0&#x60; — Does **not** remove the logs. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200294_result_data import InlineResponse200294ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200294ResultData from a JSON string
inline_response200294_result_data_instance = InlineResponse200294ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200294ResultData.to_json())

# convert the object into a dict
inline_response200294_result_data_dict = inline_response200294_result_data_instance.to_dict()
# create an instance of InlineResponse200294ResultData from a dict
inline_response200294_result_data_from_dict = InlineResponse200294ResultData.from_dict(inline_response200294_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200572ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier for the scan. A valid string. | [optional] 
**log** | **str** | The absolute path to the log file for the scan. | [optional] 
**sse_url** | **str** | The SSE interface that other applications can use to track the progress of the scan.  **Note:**  For more information about the SSE interface, read the [Server Sent Events](#server-sent-events-sse) section. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200572_result_data import InlineResponse200572ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200572ResultData from a JSON string
inline_response200572_result_data_instance = InlineResponse200572ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200572ResultData.to_json())

# convert the object into a dict
inline_response200572_result_data_dict = inline_response200572_result_data_instance.to_dict()
# create an instance of InlineResponse200572ResultData from a dict
inline_response200572_result_data_from_dict = InlineResponse200572ResultData.from_dict(inline_response200572_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



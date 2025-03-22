# InlineResponse200255ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmdline** | **str** | Information about the FTP process, from the &#x60;ps&#x60; ([process status](http://www.linfo.org/ps.html)) command. | [optional] 
**file** | **str** | The file that the session is processing.  **Note:**  The function returns a blank value if the session is idle. | [optional] 
**host** | [**InlineResponse200255ResultDataHost**](InlineResponse200255ResultDataHost.md) |  | [optional] 
**login** | **str** | The FTP session login time. | [optional] 
**pid** | **int** | The session&#39;s PID. | [optional] 
**status** | **str** | The session&#39;s status. - &#x60;IDLE&#x60; - The session is connected, but idle. - &#x60;DL&#x60; - A download is in progress. - &#x60;UL&#x60; - An upload is in progress. | [optional] 
**user** | **str** | The FTP account username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200255_result_data import InlineResponse200255ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200255ResultData from a JSON string
inline_response200255_result_data_instance = InlineResponse200255ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200255ResultData.to_json())

# convert the object into a dict
inline_response200255_result_data_dict = inline_response200255_result_data_instance.to_dict()
# create an instance of InlineResponse200255ResultData from a dict
inline_response200255_result_data_from_dict = InlineResponse200255ResultData.from_dict(inline_response200255_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



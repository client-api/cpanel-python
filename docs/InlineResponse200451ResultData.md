# InlineResponse200451ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | An error message about why system couldn&#39;t read a resource&#39;s status file. | [optional] 
**name** | **str** | The cPanel services, devices, and server health check points on the server.  * A valid [cPanel service](https://go.cpanel.net/ThecPanelWHMServiceDaemons).  * &#x60;CPU Count&#x60; — The number of CPUs on the server. * &#x60;Disk mount (mount)&#x60; — The server&#39;s disk mounts, where &#x60;mount&#x60; represents the disk mount location. * &#x60;Server Load&#x60; — The server&#39;s CPU load. * &#x60;Memory Used&#x60; — The server&#39;s current memory use. * &#x60;Swap&#x60; — The server&#39;s swap space. | [optional] 
**status** | [**InlineResponse200451ResultDataStatus**](InlineResponse200451ResultDataStatus.md) |  | [optional] 
**type** | **str** | The type of resource.  * &#x60;device&#x60; * &#x60;metric&#x60; * &#x60;service&#x60; | [optional] 
**value** | [**InlineResponse200451ResultDataValue**](InlineResponse200451ResultDataValue.md) |  | [optional] 
**version** | **str** | The resource&#39;s software version.  **Important:**  The function **only** returns this value if a valid software version exists. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200451_result_data import InlineResponse200451ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200451ResultData from a JSON string
inline_response200451_result_data_instance = InlineResponse200451ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200451ResultData.to_json())

# convert the object into a dict
inline_response200451_result_data_dict = inline_response200451_result_data_instance.to_dict()
# create an instance of InlineResponse200451ResultData from a dict
inline_response200451_result_data_from_dict = InlineResponse200451ResultData.from_dict(inline_response200451_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



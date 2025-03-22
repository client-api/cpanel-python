# InlineResponse200556ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_running** | **int** | Whether any backups are in progess. * &#x60;1&#x60; - Backups are in progress. * &#x60;0&#x60; - No backups are in progress. | [optional] 
**sites** | [**List[InlineResponse200556ResultDataSites]**](InlineResponse200556ResultDataSites.md) | An array that contains each site with a backup in progress. The function only populates this array if it is actively processing a backup. | [optional] 
**sse_url** | **str** | The SSE service URL that the system uses to monitor the backup progress. The SSE service URL does not contain a protocol, hostname, or port. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200556_result_data import InlineResponse200556ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200556ResultData from a JSON string
inline_response200556_result_data_instance = InlineResponse200556ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200556ResultData.to_json())

# convert the object into a dict
inline_response200556_result_data_dict = inline_response200556_result_data_instance.to_dict()
# create an instance of InlineResponse200556ResultData from a dict
inline_response200556_result_data_from_dict = InlineResponse200556ResultData.from_dict(inline_response200556_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



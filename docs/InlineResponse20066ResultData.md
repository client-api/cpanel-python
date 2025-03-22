# InlineResponse20066ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_file** | **str** | The current file being scanned. | [optional] 
**infected_files** | **List[str]** | List of files scanned and found to be infected. | [optional] 
**scan_complete** | **int** | Whether the last scan has completed. * &#x60;1&#x60; - scan has completed. * &#x60;0&#x60; - scan has **not** completed. | [optional] 
**scanned_file_count** | **int** | The number of files already scanned. | [optional] 
**scanned_file_size** | **int** | The number of bytes of data scanned. | [optional] 
**time_started** | **str** | The epoch timestamp of the beginning of the last scan. | [optional] 
**total_file_count** | **int** | The total number of files found to scan. | [optional] 
**total_file_size_mi_b** | **int** | The total number of megabytes of data found to scan. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20066_result_data import InlineResponse20066ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20066ResultData from a JSON string
inline_response20066_result_data_instance = InlineResponse20066ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20066ResultData.to_json())

# convert the object into a dict
inline_response20066_result_data_dict = inline_response20066_result_data_instance.to_dict()
# create an instance of InlineResponse20066ResultData from a dict
inline_response20066_result_data_from_dict = InlineResponse20066ResultData.from_dict(inline_response20066_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



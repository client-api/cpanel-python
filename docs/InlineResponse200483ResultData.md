# InlineResponse200483ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The publish process&#39;s log file name.  **Note:**  The system stores this file in the &#x60;logs/&#x60; directory, relative to the cPanel account&#39;s home directory. | [optional] 
**pid** | **int** | The publish action&#39;s process ID. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200483_result_data import InlineResponse200483ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200483ResultData from a JSON string
inline_response200483_result_data_instance = InlineResponse200483ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200483ResultData.to_json())

# convert the object into a dict
inline_response200483_result_data_dict = inline_response200483_result_data_instance.to_dict()
# create an instance of InlineResponse200483ResultData from a dict
inline_response200483_result_data_from_dict = InlineResponse200483ResultData.from_dict(inline_response200483_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse2008ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **str** | The log file&#39;s restoration identification (ID). The system uses the backup restoration&#39;s date to create this ID. The ID is in [ISO-8601 Date Time](https://en.wikipedia.org/wiki/ISO_8601) format with the log&#39;s revision number appended. | [optional] 
**log_path** | **str** | The filepath to the backup restoration&#39;s log file. | [optional] 
**messages** | **List[str]** | An array of statements about the database&#39;s restoration. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2008_result_data import InlineResponse2008ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2008ResultData from a JSON string
inline_response2008_result_data_instance = InlineResponse2008ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2008ResultData.to_json())

# convert the object into a dict
inline_response2008_result_data_dict = inline_response2008_result_data_instance.to_dict()
# create an instance of InlineResponse2008ResultData from a dict
inline_response2008_result_data_from_dict = InlineResponse2008ResultData.from_dict(inline_response2008_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



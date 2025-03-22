# InlineResponse200384ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | The database name. | [optional] 
**disk_usage** | **int** | The disk space that the database uses, in bytes. | [optional] 
**users** | **List[str]** | An array of database usernames.  **Note:**    If no users exist on a database, the function returns an empty array | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200384_result_data import InlineResponse200384ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200384ResultData from a JSON string
inline_response200384_result_data_instance = InlineResponse200384ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200384ResultData.to_json())

# convert the object into a dict
inline_response200384_result_data_dict = inline_response200384_result_data_instance.to_dict()
# create an instance of InlineResponse200384ResultData from a dict
inline_response200384_result_data_from_dict = InlineResponse200384ResultData.from_dict(inline_response200384_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



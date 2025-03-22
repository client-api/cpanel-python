# InlineResponse200351ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | **List[str]** | An array of databases that belong to the database user.  **Note:**  If no users are assigned to a database, the function returns an empty array. | [optional] 
**shortuser** | **str** | The short version of the database username. | [optional] 
**user** | **str** | The database username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200351_result_data import InlineResponse200351ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200351ResultData from a JSON string
inline_response200351_result_data_instance = InlineResponse200351ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200351ResultData.to_json())

# convert the object into a dict
inline_response200351_result_data_dict = inline_response200351_result_data_instance.to_dict()
# create an instance of InlineResponse200351ResultData from a dict
inline_response200351_result_data_from_dict = InlineResponse200351ResultData.from_dict(inline_response200351_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



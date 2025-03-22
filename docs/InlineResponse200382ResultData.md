# InlineResponse200382ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_database_name_length** | **int** | The maximum length of a database name. | [optional] 
**max_username_length** | **int** | The maximum length of a database username. | [optional] 
**prefix** | **str** | If database prefixing is enabled, this return outputs the database prefix. A valid string up to eight characters and an underscore (&#x60;_&#x60;). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200382_result_data import InlineResponse200382ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200382ResultData from a JSON string
inline_response200382_result_data_instance = InlineResponse200382ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200382ResultData.to_json())

# convert the object into a dict
inline_response200382_result_data_dict = inline_response200382_result_data_instance.to_dict()
# create an instance of InlineResponse200382ResultData from a dict
inline_response200382_result_data_from_dict = InlineResponse200382ResultData.from_dict(inline_response200382_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



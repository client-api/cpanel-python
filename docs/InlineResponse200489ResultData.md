# InlineResponse200489ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | The date that the system recorded the error. | [optional] 
**entry** | **str** | The error log entry. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200489_result_data import InlineResponse200489ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200489ResultData from a JSON string
inline_response200489_result_data_instance = InlineResponse200489ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200489ResultData.to_json())

# convert the object into a dict
inline_response200489_result_data_dict = inline_response200489_result_data_instance.to_dict()
# create an instance of InlineResponse200489ResultData from a dict
inline_response200489_result_data_from_dict = InlineResponse200489ResultData.from_dict(inline_response200489_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



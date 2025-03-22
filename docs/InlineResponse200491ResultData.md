# InlineResponse200491ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | The current date and time. | [optional] 
**url** | **str** | The URL of the file from which the system generates statistics reports. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200491_result_data import InlineResponse200491ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200491ResultData from a JSON string
inline_response200491_result_data_instance = InlineResponse200491ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200491ResultData.to_json())

# convert the object into a dict
inline_response200491_result_data_dict = inline_response200491_result_data_instance.to_dict()
# create an instance of InlineResponse200491ResultData from a dict
inline_response200491_result_data_from_dict = InlineResponse200491ResultData.from_dict(inline_response200491_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



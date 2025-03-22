# InlineResponse200500ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Maximum number of team users with roles.  **Note:**  This value is stored in the package. | [optional] 
**used** | **int** | The current number of team users with roles. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200500_result_data import InlineResponse200500ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200500ResultData from a JSON string
inline_response200500_result_data_instance = InlineResponse200500ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200500ResultData.to_json())

# convert the object into a dict
inline_response200500_result_data_dict = inline_response200500_result_data_instance.to_dict()
# create an instance of InlineResponse200500ResultData from a dict
inline_response200500_result_data_from_dict = InlineResponse200500ResultData.from_dict(inline_response200500_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



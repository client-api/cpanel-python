# InlineResponse200538ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The task&#39;s action.  * &#x60;create&#x60;  **Note:**  &#x60;create&#x60; is the only possible value. | [optional] 
**args** | [**InlineResponse200538ResultArgs**](InlineResponse200538ResultArgs.md) |  | [optional] 
**id** | **str** | The task&#39;s ID number. | [optional] 
**subsystem** | **str** | The subsystem that will handle the process.  * &#x60;VersionControl&#x60;  **Note:**  &#x60;VersionControl&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200538_result_data import InlineResponse200538ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200538ResultData from a JSON string
inline_response200538_result_data_instance = InlineResponse200538ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200538ResultData.to_json())

# convert the object into a dict
inline_response200538_result_data_dict = inline_response200538_result_data_instance.to_dict()
# create an instance of InlineResponse200538ResultData from a dict
inline_response200538_result_data_from_dict = InlineResponse200538ResultData.from_dict(inline_response200538_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200299ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The mailbox GUID. | [optional] 
**mailbox** | **str** | The mailbox name. | [optional] 
**messages** | **int** | The number of messages in the folder. | [optional] 
**vsize** | **int** | The size of the folder, in bytes. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200299_result_data import InlineResponse200299ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200299ResultData from a JSON string
inline_response200299_result_data_instance = InlineResponse200299ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200299ResultData.to_json())

# convert the object into a dict
inline_response200299_result_data_dict = inline_response200299_result_data_instance.to_dict()
# create an instance of InlineResponse200299ResultData from a dict
inline_response200299_result_data_from_dict = InlineResponse200299ResultData.from_dict(inline_response200299_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200517ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | The API token&#39;s creation date and time. | [optional] 
**token** | **str** | The generated API token. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200517_result_data import InlineResponse200517ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200517ResultData from a JSON string
inline_response200517_result_data_instance = InlineResponse200517ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200517ResultData.to_json())

# convert the object into a dict
inline_response200517_result_data_dict = inline_response200517_result_data_instance.to_dict()
# create an instance of InlineResponse200517ResultData from a dict
inline_response200517_result_data_from_dict = InlineResponse200517ResultData.from_dict(inline_response200517_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



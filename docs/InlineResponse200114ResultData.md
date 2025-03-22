# InlineResponse200114ResultData

Information about the newly-created DDNS domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **int** | The creation time of the Dynamic DNS domain. | [optional] 
**id** | **str** | The DDNS domain’s ID. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200114_result_data import InlineResponse200114ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200114ResultData from a JSON string
inline_response200114_result_data_instance = InlineResponse200114ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200114ResultData.to_json())

# convert the object into a dict
inline_response200114_result_data_dict = inline_response200114_result_data_instance.to_dict()
# create an instance of InlineResponse200114ResultData from a dict
inline_response200114_result_data_from_dict = InlineResponse200114ResultData.from_dict(inline_response200114_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



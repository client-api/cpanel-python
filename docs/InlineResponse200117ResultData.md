# InlineResponse200117ResultData

Information about the DDNS domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The DDNS domain’s new ID. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200117_result_data import InlineResponse200117ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200117ResultData from a JSON string
inline_response200117_result_data_instance = InlineResponse200117ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200117ResultData.to_json())

# convert the object into a dict
inline_response200117_result_data_dict = inline_response200117_result_data_instance.to_dict()
# create an instance of InlineResponse200117ResultData from a dict
inline_response200117_result_data_from_dict = InlineResponse200117ResultData.from_dict(inline_response200117_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



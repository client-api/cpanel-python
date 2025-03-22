# InlineResponse200325ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | **str** | The handler&#39;s extension. A valid file extension. | [optional] 
**handler** | **str** | The handler&#39;s name. A valid string. | [optional] 
**origin** | **str** | The handler&#39;s owner. - system - user | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200325_result_data import InlineResponse200325ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200325ResultData from a JSON string
inline_response200325_result_data_instance = InlineResponse200325ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200325ResultData.to_json())

# convert the object into a dict
inline_response200325_result_data_dict = inline_response200325_result_data_instance.to_dict()
# create an instance of InlineResponse200325ResultData from a dict
inline_response200325_result_data_from_dict = InlineResponse200325ResultData.from_dict(inline_response200325_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



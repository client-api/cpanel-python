# InlineResponse200557ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **int** | Whether the system cancelled an active backup. * &#x60;1&#x60; — Backup cancelled. * &#x60;0&#x60; — Could not cancel the backup or no active backup in progress. | [optional] 
**site** | **str** | The site&#39;s URL without the protocol prefix. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200557_result_data import InlineResponse200557ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200557ResultData from a JSON string
inline_response200557_result_data_instance = InlineResponse200557ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200557ResultData.to_json())

# convert the object into a dict
inline_response200557_result_data_dict = inline_response200557_result_data_instance.to_dict()
# create an instance of InlineResponse200557ResultData from a dict
inline_response200557_result_data_from_dict = InlineResponse200557ResultData.from_dict(inline_response200557_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



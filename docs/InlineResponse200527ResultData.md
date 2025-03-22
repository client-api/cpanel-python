# InlineResponse200527ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**InlineResponse200527ResultDataAccounts**](InlineResponse200527ResultDataAccounts.md) |  | [optional] 
**conflict** | **int** | Whether the system detected an account conflict.  * &#x60;1&#x60; — Conflict. * &#x60;0&#x60; — **No** conflict. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data import InlineResponse200527ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultData from a JSON string
inline_response200527_result_data_instance = InlineResponse200527ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultData.to_json())

# convert the object into a dict
inline_response200527_result_data_dict = inline_response200527_result_data_instance.to_dict()
# create an instance of InlineResponse200527ResultData from a dict
inline_response200527_result_data_from_dict = InlineResponse200527ResultData.from_dict(inline_response200527_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



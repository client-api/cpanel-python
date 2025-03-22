# InlineResponse20047ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegatee** | **str** | The user with delegation rights. | [optional] 
**delegator** | **str** | The calendar&#39;s owner. | [optional] 
**read_only** | **int** | Whether the delegatee has read-only access on the calendar. * &#x60;1&#x60; - Read-only access. * &#x60;0&#x60; - Full access. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20047_result_data import InlineResponse20047ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20047ResultData from a JSON string
inline_response20047_result_data_instance = InlineResponse20047ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20047ResultData.to_json())

# convert the object into a dict
inline_response20047_result_data_dict = inline_response20047_result_data_instance.to_dict()
# create an instance of InlineResponse20047ResultData from a dict
inline_response20047_result_data_from_dict = InlineResponse20047ResultData.from_dict(inline_response20047_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



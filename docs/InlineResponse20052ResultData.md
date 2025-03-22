# InlineResponse20052ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar** | **str** | The calendar id. | [optional] 
**calname** | **str** | The name of the calendar. | [optional] 
**delegatee** | **str** | The person to whom the owner of the calendar shared it. | [optional] 
**delegator** | **str** | The owner of the calendar. | [optional] 
**readonly** | **int** | If set to &#x60;1&#x60;, the &#x60;delegatee&#x60; only has read access to the calendar. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20052_result_data import InlineResponse20052ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20052ResultData from a JSON string
inline_response20052_result_data_instance = InlineResponse20052ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20052ResultData.to_json())

# convert the object into a dict
inline_response20052_result_data_dict = inline_response20052_result_data_instance.to_dict()
# create an instance of InlineResponse20052ResultData from a dict
inline_response20052_result_data_from_dict = InlineResponse20052ResultData.from_dict(inline_response20052_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



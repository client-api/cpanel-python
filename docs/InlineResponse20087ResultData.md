# InlineResponse20087ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_name** | **str** | The DNS zone in which the system updated the domain&#39;s record. | [optional] 
**record_name** | **str** | The name of the domain&#39;s updated DNS record. | [optional] 
**record_type** | **str** | The type of the DNS record which was updated. | [optional] 
**old_value** | **str** | The value of the DNS record before it was updated. | [optional] 
**new_value** | **str** | The value of the DNS record after it was updated. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20087_result_data import InlineResponse20087ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20087ResultData from a JSON string
inline_response20087_result_data_instance = InlineResponse20087ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20087ResultData.to_json())

# convert the object into a dict
inline_response20087_result_data_dict = inline_response20087_result_data_instance.to_dict()
# create an instance of InlineResponse20087ResultData from a dict
inline_response20087_result_data_from_dict = InlineResponse20087ResultData.from_dict(inline_response20087_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



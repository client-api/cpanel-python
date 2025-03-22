# InlineResponse200459ResultDataSystems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the system. | [optional] 
**description** | **str** | A description of the system. | [optional] 
**domain** | **str** | The system&#39;s base domain. | [optional] 
**id** | **int** | The system&#39;s ID number. | [optional] 
**interval** | **str** | The time interval for monitoring checks. | [optional] 
**limits** | [**InlineResponse200459ResultDataLimits**](InlineResponse200459ResultDataLimits.md) |  | [optional] 
**system_type** | [**InlineResponse200459ResultDataSystemType**](InlineResponse200459ResultDataSystemType.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200459_result_data_systems import InlineResponse200459ResultDataSystems

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200459ResultDataSystems from a JSON string
inline_response200459_result_data_systems_instance = InlineResponse200459ResultDataSystems.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200459ResultDataSystems.to_json())

# convert the object into a dict
inline_response200459_result_data_systems_dict = inline_response200459_result_data_systems_instance.to_dict()
# create an instance of InlineResponse200459ResultDataSystems from a dict
inline_response200459_result_data_systems_from_dict = InlineResponse200459ResultDataSystems.from_dict(inline_response200459_result_data_systems_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



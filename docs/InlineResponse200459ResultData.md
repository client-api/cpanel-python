# InlineResponse200459ResultData

An object that contains project attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The project ID number. | [optional] 
**identifier** | **str** | The project identifier. | [optional] 
**location** | **str** | The region where monitoring checks originate. | [optional] 
**name** | **str** | The project&#39;s name. | [optional] 
**role** | [**InlineResponse200459ResultDataRole**](InlineResponse200459ResultDataRole.md) |  | [optional] 
**systems** | [**List[InlineResponse200459ResultDataSystems]**](InlineResponse200459ResultDataSystems.md) | Information about the system that the project monitors. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200459_result_data import InlineResponse200459ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200459ResultData from a JSON string
inline_response200459_result_data_instance = InlineResponse200459ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200459ResultData.to_json())

# convert the object into a dict
inline_response200459_result_data_dict = inline_response200459_result_data_instance.to_dict()
# create an instance of InlineResponse200459ResultData from a dict
inline_response200459_result_data_from_dict = InlineResponse200459ResultData.from_dict(inline_response200459_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



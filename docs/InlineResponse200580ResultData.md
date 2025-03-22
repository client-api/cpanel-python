# InlineResponse200580ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon** | **str** | The name of the cPAddon in double colon-delimited form. | [optional] 
**domain** | **str** | The domain on which the instance is installed. | [optional] 
**installdir** | **str** | The full path of the directory in which the system deployed the cPAddon. | [optional] 
**instance** | **str** | The name of the instance and the number suffix. | [optional] 
**unique_id** | **str** | The unique identifier for the cPAddon.  **Note:**   This identifier will not change when you change the cPAddon&#39;s settings. However, if a new instance reuses a cPaddon&#39;s instance name, the system updates the unique identifier. You can use this identifier to select a specific instance to modify. A unique identifier. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200580_result_data import InlineResponse200580ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200580ResultData from a JSON string
inline_response200580_result_data_instance = InlineResponse200580ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200580ResultData.to_json())

# convert the object into a dict
inline_response200580_result_data_dict = inline_response200580_result_data_instance.to_dict()
# create an instance of InlineResponse200580ResultData from a dict
inline_response200580_result_data_from_dict = InlineResponse200580ResultData.from_dict(inline_response200580_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200568ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | This array contains the errors that the system experienced while it retrieved the instances. | [optional] 
**instances** | [**List[InlineResponse200568ResultDataInstances]**](InlineResponse200568ResultDataInstances.md) | This array of objects contains the WordPress instance information. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200568_result_data import InlineResponse200568ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200568ResultData from a JSON string
inline_response200568_result_data_instance = InlineResponse200568ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200568ResultData.to_json())

# convert the object into a dict
inline_response200568_result_data_dict = inline_response200568_result_data_instance.to_dict()
# create an instance of InlineResponse200568ResultData from a dict
inline_response200568_result_data_from_dict = InlineResponse200568ResultData.from_dict(inline_response200568_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



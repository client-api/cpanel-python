# InlineResponse200278ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | An array of errors that the system generated. | [optional] 
**failure_type** | **str** | The reason why the system will register the hostname. * &#x60;new&#x60; — The host does **not** already exist. * &#x60;changed&#x60; — The host&#39;s information has changed. | [optional] 
**host** | [**List[InlineResponse200278ResultDataHost]**](InlineResponse200278ResultDataHost.md) | An array of objects that contain information about the host. | [optional] 
**status** | **int** | Whether the host already exists in the &#x60;/home/user/.ssh/known_hosts&#x60; file, where &#x60;user&#x60; is the cPanel account username. * &#x60;1&#x60; — Exists. * &#x60;0&#x60; — The host does **not** already exist, or the system must re-register the hostname. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200278_result_data import InlineResponse200278ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200278ResultData from a JSON string
inline_response200278_result_data_instance = InlineResponse200278ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200278ResultData.to_json())

# convert the object into a dict
inline_response200278_result_data_dict = inline_response200278_result_data_instance.to_dict()
# create an instance of InlineResponse200278ResultData from a dict
inline_response200278_result_data_from_dict = InlineResponse200278ResultData.from_dict(inline_response200278_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



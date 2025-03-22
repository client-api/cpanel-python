# InlineResponse200544ResultLastDeployment

An object containing information about the commit that the system most recently deployed.  **Note:**  The system **only** returns this object if deployment information exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_date** | **int** | The timestamp for the most-recent deployment. | [optional] 
**repository_state** | [**InlineResponse200544ResultLastDeploymentRepositoryState**](InlineResponse200544ResultLastDeploymentRepositoryState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200544_result_last_deployment import InlineResponse200544ResultLastDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200544ResultLastDeployment from a JSON string
inline_response200544_result_last_deployment_instance = InlineResponse200544ResultLastDeployment.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200544ResultLastDeployment.to_json())

# convert the object into a dict
inline_response200544_result_last_deployment_dict = inline_response200544_result_last_deployment_instance.to_dict()
# create an instance of InlineResponse200544ResultLastDeployment from a dict
inline_response200544_result_last_deployment_from_dict = InlineResponse200544ResultLastDeployment.from_dict(inline_response200544_result_last_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200544ResultLastDeploymentRepositoryState

A object containing information about the state of the repository at the time of the most recent deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author&#39;s name and email address for the commit that the system most recently deployed. | [optional] 
**var_date** | **int** | The timestamp for the commit that the system most recently deployed. | [optional] 
**identifier** | **str** | The identifier (SHA-1 value) for the commit that the system most recently deployed. | [optional] 
**message** | **str** | The commit message for the commit that the system most recently deployed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200544_result_last_deployment_repository_state import InlineResponse200544ResultLastDeploymentRepositoryState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200544ResultLastDeploymentRepositoryState from a JSON string
inline_response200544_result_last_deployment_repository_state_instance = InlineResponse200544ResultLastDeploymentRepositoryState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200544ResultLastDeploymentRepositoryState.to_json())

# convert the object into a dict
inline_response200544_result_last_deployment_repository_state_dict = inline_response200544_result_last_deployment_repository_state_instance.to_dict()
# create an instance of InlineResponse200544ResultLastDeploymentRepositoryState from a dict
inline_response200544_result_last_deployment_repository_state_from_dict = InlineResponse200544ResultLastDeploymentRepositoryState.from_dict(inline_response200544_result_last_deployment_repository_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



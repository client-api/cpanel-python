# InlineResponse200545ResultDataLastDeployment

An object containing information about the commit that the system most recently deployed.  **Note:**  If no deployment information exists, the function returns a `null` value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_date** | **int** | The timestamp for the most recent deployment. | [optional] 
**repository_state** | [**InlineResponse200544ResultLastDeploymentRepositoryState**](InlineResponse200544ResultLastDeploymentRepositoryState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200545_result_data_last_deployment import InlineResponse200545ResultDataLastDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200545ResultDataLastDeployment from a JSON string
inline_response200545_result_data_last_deployment_instance = InlineResponse200545ResultDataLastDeployment.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200545ResultDataLastDeployment.to_json())

# convert the object into a dict
inline_response200545_result_data_last_deployment_dict = inline_response200545_result_data_last_deployment_instance.to_dict()
# create an instance of InlineResponse200545ResultDataLastDeployment from a dict
inline_response200545_result_data_last_deployment_from_dict = InlineResponse200545ResultDataLastDeployment.from_dict(inline_response200545_result_data_last_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



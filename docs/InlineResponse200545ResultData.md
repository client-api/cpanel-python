# InlineResponse200545ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_branches** | **List[Optional[str]]** | A list of local and remote branches available for the cloned or existing repository.  * An empty array, if no branches exist. * &#x60;null&#x60; — The repository is a bare repository. | [optional] 
**branch** | **str** | The repository&#39;s current branch.  * &#x60;null&#x60; — The system has not finished the clone process for the repository, no local branches exist, or the repository is a bare repository. | [optional] 
**clone_urls** | [**InlineResponse200545ResultDataCloneUrls**](InlineResponse200545ResultDataCloneUrls.md) |  | [optional] 
**deployable** | **int** | Whether the system could deploy the repository.  * &#x60;1&#x60; — Can deploy. * &#x60;0&#x60; — Cannot deploy. | [optional] 
**last_deployment** | [**InlineResponse200545ResultDataLastDeployment**](InlineResponse200545ResultDataLastDeployment.md) |  | [optional] 
**last_update** | [**InlineResponse200545ResultDataLastUpdate**](InlineResponse200545ResultDataLastUpdate.md) |  | [optional] 
**name** | **str** | The repository&#39;s display name. | [optional] 
**repository_root** | **str** | The directory path that exists in the user&#39;s &#x60;home&#x60; directory containing the repository. | [optional] 
**source_repository** | [**InlineResponse200545ResultDataSourceRepository**](InlineResponse200545ResultDataSourceRepository.md) |  | [optional] 
**tasks** | [**List[InlineResponse200545ResultDataTasks]**](InlineResponse200545ResultDataTasks.md) | An array of objects containing information about the [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) system&#39;s process that will clone the repository.  **Note:**  The function **only** returns this value if the clone process is not finished. | [optional] 
**type** | **str** | The repository type.  * &#x60;git&#x60; — A [Git](https://git-scm.com/) repository.  **Note:**  * &#x60;git&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200545_result_data import InlineResponse200545ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200545ResultData from a JSON string
inline_response200545_result_data_instance = InlineResponse200545ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200545ResultData.to_json())

# convert the object into a dict
inline_response200545_result_data_dict = inline_response200545_result_data_instance.to_dict()
# create an instance of InlineResponse200545ResultData from a dict
inline_response200545_result_data_from_dict = InlineResponse200545ResultData.from_dict(inline_response200545_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



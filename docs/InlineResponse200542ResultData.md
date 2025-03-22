# InlineResponse200542ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_branches** | **List[str]** | An list of available branches for the cloned or existing repository, if any exist. | [optional] 
**branch** | **str** | The repository&#39;s current branch.  * &#x60;null&#x60; — The system has **not** finished the clone process for the repository, or no local branches exist. | [optional] 
**clone_urls** | [**InlineResponse200542ResultDataCloneUrls**](InlineResponse200542ResultDataCloneUrls.md) |  | [optional] 
**last_update** | **str** | Information about the most-recent (HEAD) commit for the current branch.  **Note:**  * The system may require a large amount of time to clone large repositories. Until this process finishes, HEAD information is unavailable. * &#x60;null&#x60; is the only possible value. | [optional] 
**name** | **str** | The repository&#39;s display name. | [optional] 
**repository_root** | **str** | The absolute path of the directory that contains the repository in the user&#39;s &#x60;home&#x60; directory. | [optional] 
**source_repository** | [**InlineResponse200542ResultDataSourceRepository**](InlineResponse200542ResultDataSourceRepository.md) |  | [optional] 
**tasks** | [**List[InlineResponse200542ResultDataTasks]**](InlineResponse200542ResultDataTasks.md) | An array of objects containing information about the [Task Queue](https://go.cpanel.net/whmdocsTaskQueueMonitor) system&#39;s process that will clone the repository.  **Note:**  The function **only** returns this value if it will clone a repository. | [optional] 
**type** | **str** | The repository type.  * &#x60;git&#x60; — A Git repostiory.  **Note:**  &#x60;git&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200542_result_data import InlineResponse200542ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200542ResultData from a JSON string
inline_response200542_result_data_instance = InlineResponse200542ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200542ResultData.to_json())

# convert the object into a dict
inline_response200542_result_data_dict = inline_response200542_result_data_instance.to_dict()
# create an instance of InlineResponse200542ResultData from a dict
inline_response200542_result_data_from_dict = InlineResponse200542ResultData.from_dict(inline_response200542_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



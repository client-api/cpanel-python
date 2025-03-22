# InlineResponse200548ResultRepositoryState

An object containing information about the repository's state at the time of deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The most-recent commit&#39;s author&#39;s name and email address as they exist in the user&#39;s Git configuration files. | [optional] 
**branch** | **str** | The repository&#39;s current branch. | [optional] 
**var_date** | **int** | The timestamp for the most-recent commit, in Unix time format. | [optional] 
**identifier** | **str** | The identifier (SHA-1 value) for the most-recent commit. | [optional] 
**message** | **str** | The commit message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200548_result_repository_state import InlineResponse200548ResultRepositoryState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200548ResultRepositoryState from a JSON string
inline_response200548_result_repository_state_instance = InlineResponse200548ResultRepositoryState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200548ResultRepositoryState.to_json())

# convert the object into a dict
inline_response200548_result_repository_state_dict = inline_response200548_result_repository_state_instance.to_dict()
# create an instance of InlineResponse200548ResultRepositoryState from a dict
inline_response200548_result_repository_state_from_dict = InlineResponse200548ResultRepositoryState.from_dict(inline_response200548_result_repository_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



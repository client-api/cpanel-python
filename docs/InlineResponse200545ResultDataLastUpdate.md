# InlineResponse200545ResultDataLastUpdate

An object containing information about the most recent (HEAD) commit for the current branch.  **Note:**  This object's information resembles the output of the `git log -1` command.  **Important:**  * If the repository does **not** include any commits, the function returns a `null` value instead of an object. * The system may require a large amount of time to clone larger repositories. Until this process finishes, HEAD information is unavailable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The most recent commit&#39;s author name and email address. | [optional] 
**var_date** | **int** | The timestamp for the most recent commit. | [optional] 
**identifier** | **str** | The identifier (SHA-1 value) for the most recent commit. | [optional] 
**message** | **str** | The commit message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200545_result_data_last_update import InlineResponse200545ResultDataLastUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200545ResultDataLastUpdate from a JSON string
inline_response200545_result_data_last_update_instance = InlineResponse200545ResultDataLastUpdate.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200545ResultDataLastUpdate.to_json())

# convert the object into a dict
inline_response200545_result_data_last_update_dict = inline_response200545_result_data_last_update_instance.to_dict()
# create an instance of InlineResponse200545ResultDataLastUpdate from a dict
inline_response200545_result_data_last_update_from_dict = InlineResponse200545ResultDataLastUpdate.from_dict(inline_response200545_result_data_last_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



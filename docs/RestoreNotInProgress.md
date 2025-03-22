# RestoreNotInProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_running** | **int** | Whether the system is processing a backup restoration.  * &#x60;0&#x60; - No restoration in progress. This is the only possible value. | [optional] 
**last_outcome** | [**RestoreNotInProgressLastOutcome**](RestoreNotInProgressLastOutcome.md) |  | [optional] 
**sites** | **object** | Information about the site that the system is actively restoring.  **Note:**  * This function returns an empty array when there is **not** an active backup restoration. This is the only possible value. * We have not implemented this return. | [optional] 

## Example

```python
from clientapi_cpanel.models.restore_not_in_progress import RestoreNotInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreNotInProgress from a JSON string
restore_not_in_progress_instance = RestoreNotInProgress.from_json(json)
# print the JSON string representation of the object
print(RestoreNotInProgress.to_json())

# convert the object into a dict
restore_not_in_progress_dict = restore_not_in_progress_instance.to_dict()
# create an instance of RestoreNotInProgress from a dict
restore_not_in_progress_from_dict = RestoreNotInProgress.from_dict(restore_not_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



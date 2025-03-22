# RestoreInProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_running** | **int** | Whether the system is processing a backup restoration.  * &#x60;1&#x60; - Restoration in progress. This is the only possible value. | [optional] 
**sites** | [**List[RestoreInProgressSites]**](RestoreInProgressSites.md) | Information about the site that the system is actively restoring.  **Note:**  We have not implemented this return. | [optional] 

## Example

```python
from clientapi_cpanel.models.restore_in_progress import RestoreInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreInProgress from a JSON string
restore_in_progress_instance = RestoreInProgress.from_json(json)
# print the JSON string representation of the object
print(RestoreInProgress.to_json())

# convert the object into a dict
restore_in_progress_dict = restore_in_progress_instance.to_dict()
# create an instance of RestoreInProgress from a dict
restore_in_progress_from_dict = RestoreInProgress.from_dict(restore_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



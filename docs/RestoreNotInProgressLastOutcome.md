# RestoreNotInProgressLastOutcome

The status of the last backup restoration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Where the system encountered an error during the last backup restoration.  * The error message from the restoration log database. * &#x60;null&#x60; - No occur occurred. | [optional] 
**have_outcome** | **int** | Whether the restoration log shows a successful attempt previously occurred, successfully or unsuccessfully.  * &#x60;1&#x60; - Restoration attempt occurred. * &#x60;0&#x60; - No restoration attempt occurred. | [optional] 
**site** | **str** | The WordPress site&#39;s URL without the protocol prefix. | [optional] 
**status** | **str** | The previous restoration attempt&#39;s result.  * &#x60;success&#x60; - Successful restoration. * &#x60;error&#x60; - The attempted restoration resulted in an error. * &#x60;terminated&#x60; - The system stopped the restoration process. * &#x60;timeout&#x60; - The restoration process exceeded the allowed time limit. * &#x60;low-disk&#x60; - The server&#39;s disk space was insufficient to complete the restoration. * &#x60;low-quota&#x60; - The cPanel account&#39;s quota was insufficient to complete the restoration. | [optional] 

## Example

```python
from clientapi_cpanel.models.restore_not_in_progress_last_outcome import RestoreNotInProgressLastOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreNotInProgressLastOutcome from a JSON string
restore_not_in_progress_last_outcome_instance = RestoreNotInProgressLastOutcome.from_json(json)
# print the JSON string representation of the object
print(RestoreNotInProgressLastOutcome.to_json())

# convert the object into a dict
restore_not_in_progress_last_outcome_dict = restore_not_in_progress_last_outcome_instance.to_dict()
# create an instance of RestoreNotInProgressLastOutcome from a dict
restore_not_in_progress_last_outcome_from_dict = RestoreNotInProgressLastOutcome.from_dict(restore_not_in_progress_last_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



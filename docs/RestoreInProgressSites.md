# RestoreInProgressSites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The restore process&#39;s unique ID.  * &#x60;null&#x60; is the only possible value. * We have not implemented this return. | [optional] 
**site** | **str** | The WordPress site&#39;s URL without the protocol prefix. | [optional] 
**type** | **str** | The active process type.  * &#x60;restore&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.restore_in_progress_sites import RestoreInProgressSites

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreInProgressSites from a JSON string
restore_in_progress_sites_instance = RestoreInProgressSites.from_json(json)
# print the JSON string representation of the object
print(RestoreInProgressSites.to_json())

# convert the object into a dict
restore_in_progress_sites_dict = restore_in_progress_sites_instance.to_dict()
# create an instance of RestoreInProgressSites from a dict
restore_in_progress_sites_from_dict = RestoreInProgressSites.from_dict(restore_in_progress_sites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



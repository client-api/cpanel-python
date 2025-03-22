# StatsManagerSaveConfigurationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[StatsManagersaveConfigurationChanges]**](StatsManagersaveConfigurationChanges.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.stats_manager_save_configuration_body import StatsManagerSaveConfigurationBody

# TODO update the JSON string below
json = "{}"
# create an instance of StatsManagerSaveConfigurationBody from a JSON string
stats_manager_save_configuration_body_instance = StatsManagerSaveConfigurationBody.from_json(json)
# print the JSON string representation of the object
print(StatsManagerSaveConfigurationBody.to_json())

# convert the object into a dict
stats_manager_save_configuration_body_dict = stats_manager_save_configuration_body_instance.to_dict()
# create an instance of StatsManagerSaveConfigurationBody from a dict
stats_manager_save_configuration_body_from_dict = StatsManagerSaveConfigurationBody.from_dict(stats_manager_save_configuration_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



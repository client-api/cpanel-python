# StatsManagersaveConfigurationChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzers** | [**List[StatsManagersaveConfigurationAnalyzers]**](StatsManagersaveConfigurationAnalyzers.md) | List of log analyzer configuration objects. | [optional] 
**domain** | **str** | Domain you want to configure. | [optional] 

## Example

```python
from clientapi_cpanel.models.stats_managersave_configuration_changes import StatsManagersaveConfigurationChanges

# TODO update the JSON string below
json = "{}"
# create an instance of StatsManagersaveConfigurationChanges from a JSON string
stats_managersave_configuration_changes_instance = StatsManagersaveConfigurationChanges.from_json(json)
# print the JSON string representation of the object
print(StatsManagersaveConfigurationChanges.to_json())

# convert the object into a dict
stats_managersave_configuration_changes_dict = stats_managersave_configuration_changes_instance.to_dict()
# create an instance of StatsManagersaveConfigurationChanges from a dict
stats_managersave_configuration_changes_from_dict = StatsManagersaveConfigurationChanges.from_dict(stats_managersave_configuration_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



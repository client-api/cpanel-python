# StatsManagersaveConfigurationAnalyzers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the analyzer is turned on or off for the domain.  - &#x60;1&#x60; - the analyzer is enabled. - &#x60;0&#x60; - the analyzer is disabled. | [optional] 
**name** | **str** | Name of the analyzer.  It must be one of the following:  - &#x60;analog&#x60; - Analog weblog analyzer. - &#x60;awstats&#x60; - AWStats weblog analyzer. - &#x60;webalizer&#x60; - The Webalizer weblog analyzer. | [optional] 

## Example

```python
from clientapi_cpanel.models.stats_managersave_configuration_analyzers import StatsManagersaveConfigurationAnalyzers

# TODO update the JSON string below
json = "{}"
# create an instance of StatsManagersaveConfigurationAnalyzers from a JSON string
stats_managersave_configuration_analyzers_instance = StatsManagersaveConfigurationAnalyzers.from_json(json)
# print the JSON string representation of the object
print(StatsManagersaveConfigurationAnalyzers.to_json())

# convert the object into a dict
stats_managersave_configuration_analyzers_dict = stats_managersave_configuration_analyzers_instance.to_dict()
# create an instance of StatsManagersaveConfigurationAnalyzers from a dict
stats_managersave_configuration_analyzers_from_dict = StatsManagersaveConfigurationAnalyzers.from_dict(stats_managersave_configuration_analyzers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



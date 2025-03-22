# InlineResponse200568ResultDataInstances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_config** | **str** | The WordPress instance&#39;s configuration file location. | [optional] 
**addon_name** | **str** | The WordPress cPAddon that installed the instance. * &#x60;cPanel::Blogs::WordPress&#x60; * &#x60;cPanel::Blogs::WordPressX&#x60; * &#x60;cPanel::Blogs::WordPressUnmanaged&#x60; | [optional] 
**addon_type** | **str** | The WordPress instance&#39;s installation method. * &#x60;modern&#x60; — Installed by RPM-managed WordPress cPAddon. * &#x60;legacy&#x60; — Installed by legacy cPAddon. * &#x60;unmanaged&#x60; — Installed by third-party tool or the WordPress installer. | [optional] 
**admin_url** | **str** | The URL to the instance&#39;s administration interface. | [optional] 
**admin_username** | **str** | The administrator username the installer created at the time of installation. | [optional] 
**available_version** | **str** | This return is unused. | [optional] 
**created_on** | **int** | The WordPress instance&#39;s installation date. | [optional] 
**current_version** | **str** | This return is unused. | [optional] 
**db_name** | **str** | The WordPress instance&#39;s database name. | [optional] 
**db_prefix** | **str** | The WordPress instance&#39;s database prefix. | [optional] 
**db_server** | **str** | The WordPress instance&#39;s database server hostname. | [optional] 
**db_type** | **str** | The WordPress instance&#39;s database type.  **Note** &#x60;mysql&#x60; is the only possible value. | [optional] 
**db_username** | **str** | The WordPress instance&#39;s database username. | [optional] 
**domain** | **str** | The WordPress instance&#39;s domain. | [optional] 
**full_path** | **str** | The WordPress instance&#39;s full installation path. | [optional] 
**homedir** | **str** | The cPanel account&#39;s home directory. | [optional] 
**id** | **str** | The WordPress instance&#39;s unique identifier. | [optional] 
**import_guid** | **str** | The imported WordPress instance&#39;s unique identifier. | [optional] 
**imported_on** | **int** | The WordPress instance&#39;s import date. | [optional] 
**initial_install_version** | **str** | The WordPress instance&#39;s version number at installation. | [optional] 
**migrated_from** | **str** | The cPAddon that the system migrated the instance from. | [optional] 
**migrated_on** | **int** | The timestamp when the system migrated the instance from legacy to modern WordPress cPAddon. | [optional] 
**recent** | **int** | Whether the system added the WordPress instance in the last 24 hours. * &#x60;1&#x60; — Added recently. * &#x60;0&#x60; — Added previously. | [optional] 
**rel_path** | **str** | The WordPress instance&#39;s installation path.  **Note** This function returns an empty value if the relative path is the document root. | [optional] 
**site_url** | **str** | The WordPress instance&#39;s home page URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200568_result_data_instances import InlineResponse200568ResultDataInstances

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200568ResultDataInstances from a JSON string
inline_response200568_result_data_instances_instance = InlineResponse200568ResultDataInstances.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200568ResultDataInstances.to_json())

# convert the object into a dict
inline_response200568_result_data_instances_dict = inline_response200568_result_data_instances_instance.to_dict()
# create an instance of InlineResponse200568ResultDataInstances from a dict
inline_response200568_result_data_instances_from_dict = InlineResponse200568ResultDataInstances.from_dict(inline_response200568_result_data_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



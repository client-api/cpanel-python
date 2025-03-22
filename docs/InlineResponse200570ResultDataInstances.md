# InlineResponse200570ResultDataInstances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_config** | **str** | The WordPress instance&#39;s configuration file location. | [optional] 
**addon_name** | **str** | The WordPress cPAddon that installed the instance. * &#x60;cPanel::Blogs::WordPress&#x60; * &#x60;cPanel::Blogs::WordPressX&#x60; * &#x60;cPanel::Blogs::WordPressUnmanaged&#x60; | [optional] 
**addon_type** | **str** | The WordPress instance&#39;s installation method. * &#x60;modern&#x60; — Installed by RPM-managed WordPress cPAddon. * &#x60;legacy&#x60; — Installed by legacy cPAddon. * &#x60;unmanaged&#x60; — Installed by third-party tool or the WordPress installer. | [optional] 
**admin_url** | **str** | The URL to the instance&#39;s administration interface. | [optional] 
**admin_username** | **str** | The administrator username the installer created at the time of installation. | [optional] 
**available_version** | **str** | The latest Wordpress&#39;s version. | [optional] 
**current_version** | **str** | The WordPress instance&#39;s installed version. | [optional] 
**db_name** | **str** | The WordPress instance&#39;s database name. | [optional] 
**db_prefix** | **str** | The WordPress instance&#39;s database prefix. | [optional] 
**db_server** | **str** | The WordPress instance&#39;s database server hostname. | [optional] 
**db_type** | **str** | The WordPress instance&#39;s database type. * &#x60;mysql&#x60; * &#x60;postgres&#x60; | [optional] 
**db_username** | **str** | The WordPress instance&#39;s database username. | [optional] 
**domain** | **str** | The WordPress instance&#39;s domain. | [optional] 
**full_path** | **str** | The WordPress instance&#39;s full installation path. | [optional] 
**homedir** | **str** | The cPanel account&#39;s home directory. | [optional] 
**id** | **str** | The WordPress instance&#39;s unique identifier. | [optional] 
**initial_install_version** | **str** | The WordPress instance&#39;s version number at installation. | [optional] 
**rel_path** | **str** | The WordPress instance&#39;s installation path relative to the domain&#39;s document root. | [optional] 
**site_url** | **str** | The WordPress instance&#39;s home page URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200570_result_data_instances import InlineResponse200570ResultDataInstances

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200570ResultDataInstances from a JSON string
inline_response200570_result_data_instances_instance = InlineResponse200570ResultDataInstances.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200570ResultDataInstances.to_json())

# convert the object into a dict
inline_response200570_result_data_instances_dict = inline_response200570_result_data_instances_instance.to_dict()
# create an instance of InlineResponse200570ResultDataInstances from a dict
inline_response200570_result_data_instances_from_dict = InlineResponse200570ResultDataInstances.from_dict(inline_response200570_result_data_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



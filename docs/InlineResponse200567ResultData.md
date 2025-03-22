# InlineResponse200567ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_config** | **str** | The WordPress instance&#39;s configureation absolute file path location. | [optional] 
**addon_name** | **str** | The WordPress cPAddon used to install the instance. * &#x60;cPanel::Blogs::WordPress&#x60; * &#x60;cPanel::Blogs::WordPressX&#x60; * &#x60;cPanel::Blogs::WordPressUnmanaged&#x60; | [optional] 
**addon_type** | **str** | The WordPress instance&#39;s installation method. * &#x60;modern&#x60; — Installed by RPM-managed WordPress cPAddon. * &#x60;legacy&#x60; — Installed by legacy cPAddon. * &#x60;unmanaged&#x60; — Installed by third-party tool or the WordPress installer. | [optional] 
**admin_url** | **str** | The URL to the instance&#39;s administration interface. | [optional] 
**admin_username** | **str** | The administrator username configured at the time of installation. | [optional] 
**admins** | [**List[InlineResponse200567ResultDataAdmins]**](InlineResponse200567ResultDataAdmins.md) | A list of the WordPress instance&#39;s administrators. | [optional] 
**autoupdate** | **bool** | Whether the user enabled automatic updates. * &#x60;true&#x60; — Enabled. * &#x60;false&#x60; — Disabled. | [optional] 
**autoupdate_core_has_filter** | **bool** | Whether one of more filters modify the core autoupdate settings. * &#x60;true&#x60; — Filter(s) applied. * &#x60;false&#x60; — No filters applied.  **Note**  Typically, plugins apply filters to the autoupdate settings. | [optional] 
**autoupdate_core_major** | **bool** | Whether the user enabled automatic updates for major releases. * &#x60;true&#x60; — Enabled. * &#x60;false&#x60; — Disabled. | [optional] 
**autoupdate_core_minor** | **bool** | Whether the user enabled automatic updates for minor releases. * &#x60;true&#x60; — Enabled. * &#x60;false&#x60; — Disabled. | [optional] 
**available_version** | **str** | The lastest WordPress instance&#39;s version. | [optional] 
**created_on** | **int** | The WordPress instance&#39;s installation date. | [optional] 
**current_version** | **str** | The WordPress instance&#39;s version. | [optional] 
**db_name** | **str** | A database name. | [optional] 
**db_prefix** | **str** | A database table prefix. | [optional] 
**db_server** | **str** | The WordPress instance&#39;s database server hostname. | [optional] 
**db_type** | **str** | The WordPress instance&#39;s database type. | [optional] 
**db_username** | **str** | The WordPress instance&#39;s database username. | [optional] 
**domain** | **str** | The WordPress instance&#39;s installation domain. | [optional] 
**full_path** | **str** | The WordPress instance&#39;s full installation absolute filepath. | [optional] 
**homedir** | **str** | The cPanel account&#39;s home directory. | [optional] 
**id** | **str** | The WordPress instance&#39;s unique identifier. | [optional] 
**initial_install_version** | **str** | The WordPress instance&#39;s version at installation. | [optional] 
**recent** | **int** | Whether the system added the WordPress instance in the last 24 hours. * &#x60;1&#x60; — Added recently. * &#x60;0&#x60; — Added previously. | [optional] 
**rel_path** | **str** | The WordPress instance&#39;s installation path, relative to the damin&#39;s document root.  **Note:**  This function returns an empty value if the relative path is the document root. | [optional] 
**site_url** | **str** | The WordPress instance&#39;s home page URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200567_result_data import InlineResponse200567ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200567ResultData from a JSON string
inline_response200567_result_data_instance = InlineResponse200567ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200567ResultData.to_json())

# convert the object into a dict
inline_response200567_result_data_dict = inline_response200567_result_data_instance.to_dict()
# create an instance of InlineResponse200567ResultData from a dict
inline_response200567_result_data_from_dict = InlineResponse200567ResultData.from_dict(inline_response200567_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



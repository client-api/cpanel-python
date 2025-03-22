# InlineResponse200565ResultDataBefore

A object that contains the instance's information before conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_config** | **str** | The WordPress instance&#39;s configuration file location. | [optional] 
**addon_name** | **str** | The instance&#39;s cPAddon name. | [optional] 
**addon_type** | **str** | The instance&#39;s cPAddon type.  **Note:**  &#x60;legacy&#x60; is this only possible value. | [optional] 
**admin_url** | **str** | The instance&#39;s administrator login URL. | [optional] 
**admin_username** | **str** | The instance&#39;s administrator username. | [optional] 
**available_version** | **str** | The latest WordPress version. | [optional] 
**current_version** | **str** | The WordPress instance&#39;s installed version. | [optional] 
**db_name** | **str** | The instance&#39;s database name. | [optional] 
**db_prefix** | **str** | The instance&#39;s database prefix. | [optional] 
**db_server** | **str** | The instance&#39;s database server network path. | [optional] 
**db_type** | **str** | The instance&#39;s database type. | [optional] 
**db_username** | **str** | The instance&#39;s database username. | [optional] 
**domain** | **str** | The instance&#39;s domain name. | [optional] 
**full_path** | **str** | The instance&#39;s full installation path. | [optional] 
**homedir** | **str** | The cPanel account&#39;s home directory. | [optional] 
**id** | **str** | The instance&#39;s unique ID. | [optional] 
**initial_install_version** | **str** | The instance&#39;s original installation version. | [optional] 
**rel_path** | **str** | The relative file path to the instance&#39;s document root. | [optional] 
**site_url** | **str** | The instance&#39;s URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200565_result_data_before import InlineResponse200565ResultDataBefore

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200565ResultDataBefore from a JSON string
inline_response200565_result_data_before_instance = InlineResponse200565ResultDataBefore.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200565ResultDataBefore.to_json())

# convert the object into a dict
inline_response200565_result_data_before_dict = inline_response200565_result_data_before_instance.to_dict()
# create an instance of InlineResponse200565ResultDataBefore from a dict
inline_response200565_result_data_before_from_dict = InlineResponse200565ResultDataBefore.from_dict(inline_response200565_result_data_before_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200579ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon** | **str** | The name of the cPAddon in double colon-delimited form. | [optional] 
**admin_user** | **str** | The administrative user for the cPAddon instance. | [optional] 
**autoupdate** | **int** | Whether the system processes automatic updates for the cPAddon instance. * &#x60;1&#x60; - Automatic updates enabled. * &#x60;0&#x60; - Automatic updates disabled. | [optional] 
**db_name** | **str** | The cPAddon instance&#39;s database name. | [optional] 
**db_type** | **str** | The cPAddon instance&#39;s database type. | [optional] 
**db_user** | **str** | The cPAddon instance&#39;s database user. | [optional] 
**domain** | **str** | The domain on which the instance is installed. | [optional] 
**installdir** | **str** | The full path of the directory in which the system deployed the cPAddon. | [optional] 
**url_to_install** | **str** | The URL to access the cPAddon instance. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200579_result_data import InlineResponse200579ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200579ResultData from a JSON string
inline_response200579_result_data_instance = InlineResponse200579ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200579ResultData.to_json())

# convert the object into a dict
inline_response200579_result_data_dict = inline_response200579_result_data_instance.to_dict()
# create an instance of InlineResponse200579ResultData from a dict
inline_response200579_result_data_from_dict = InlineResponse200579ResultData.from_dict(inline_response200579_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



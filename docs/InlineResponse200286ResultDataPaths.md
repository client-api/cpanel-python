# InlineResponse200286ResultDataPaths


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account&#39;s name. | [optional] 
**documentroot** | **str** | The virtual host&#39;s document root. | [optional] 
**homedir** | **str** | The home directory. | [optional] 
**main_domain** | **int** | Whether the virtual host is the account&#39;s primary domain. * &#x60;1&#x60; - Primary domain. * &#x60;0&#x60; - **Not** the primary domain. | [optional] 
**path** | **str** | The name of the virtual host&#39;s &#x60;php.ini&#x60; file. | [optional] 
**type** | **str** | The record&#39;s type. * &#x60;home&#x60; * &#x60;vhost&#x60; | [optional] 
**version** | **str** | The default PHP version. - &#x60;ea-php##&#x60;, where &#x60;##&#x60; represents the major and minor versions of PHP (for example, &#x60;ea-php72&#x60; represents PHP 7.2). - Any custom PHP package name. | [optional] 
**vhost** | **str** | The name of the virtual host. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200286_result_data_paths import InlineResponse200286ResultDataPaths

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200286ResultDataPaths from a JSON string
inline_response200286_result_data_paths_instance = InlineResponse200286ResultDataPaths.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200286ResultDataPaths.to_json())

# convert the object into a dict
inline_response200286_result_data_paths_dict = inline_response200286_result_data_paths_instance.to_dict()
# create an instance of InlineResponse200286ResultDataPaths from a dict
inline_response200286_result_data_paths_from_dict = InlineResponse200286ResultDataPaths.from_dict(inline_response200286_result_data_paths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



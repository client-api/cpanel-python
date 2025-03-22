# InlineResponse200283ResultPhpFpmPoolParms

An object containing the domain's PHP-FPM parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pm_max_children** | **int** | The maximum number of child pages per pool. | [optional] 
**pm_max_requests** | **int** | The maximum number of requests per pool. | [optional] 
**pm_process_idle_timeout** | **int** | A specified time of idleness before the system kills an FPM child process. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200283_result_php_fpm_pool_parms import InlineResponse200283ResultPhpFpmPoolParms

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200283ResultPhpFpmPoolParms from a JSON string
inline_response200283_result_php_fpm_pool_parms_instance = InlineResponse200283ResultPhpFpmPoolParms.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200283ResultPhpFpmPoolParms.to_json())

# convert the object into a dict
inline_response200283_result_php_fpm_pool_parms_dict = inline_response200283_result_php_fpm_pool_parms_instance.to_dict()
# create an instance of InlineResponse200283ResultPhpFpmPoolParms from a dict
inline_response200283_result_php_fpm_pool_parms_from_dict = InlineResponse200283ResultPhpFpmPoolParms.from_dict(inline_response200283_result_php_fpm_pool_parms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



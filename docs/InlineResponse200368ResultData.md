# InlineResponse200368ResultData

An object describing the newly-edited application.  **Note**: `application_name` is the `name` of the application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_uri** | **str** | The URI of the application. | [optional] 
**deployment_mode** | **str** | The deployment mode of the application. | [optional] 
**domain** | **str** | The domain of the application. | [optional] 
**enabled** | **int** | Whether the application is enabled or not.    * &#x60;1&#x60; — Enabled.   * &#x60;0&#x60; — Disabled. | [optional] 
**envvars** | **object** | An object of the application’s environment variables and their values. | [optional] 
**name** | **str** | The name of the application. | [optional] 
**path** | **str** | The path of the application inside the user’s home directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200368_result_data import InlineResponse200368ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200368ResultData from a JSON string
inline_response200368_result_data_instance = InlineResponse200368ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200368ResultData.to_json())

# convert the object into a dict
inline_response200368_result_data_dict = inline_response200368_result_data_instance.to_dict()
# create an instance of InlineResponse200368ResultData from a dict
inline_response200368_result_data_from_dict = InlineResponse200368ResultData.from_dict(inline_response200368_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



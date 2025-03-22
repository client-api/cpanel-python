# InlineResponse200371ResultData

**Note**:  The top-level keys are the names of the applications.  The value is the object defined here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_uri** | **str** | The URI of the application. | [optional] 
**deployment_mode** | **str** | The deployment mode of the application.    * &#x60;development&#x60; — Sets the application to run in a development environment.   * &#x60;production&#x60; — Sets the application to run in a production environment. | [optional] 
**deps** | [**InlineResponse200371ResultDeps**](InlineResponse200371ResultDeps.md) |  | [optional] 
**domain** | **str** | The domain of the application | [optional] 
**enabled** | **object** | The application’s enabled status.  * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — Disabled. | [optional] 
**envvars** | **object** | The environment variables set for the application. | [optional] 
**name** | **str** | The name of the application | [optional] 
**nodejs** | **str** | The path of the Nodejs executable. Passenger uses Nodejs to run the application.  **Note**:  The function only returns this value if you configure this application to use Nodejs. | [optional] 
**path** | **str** | The path of the application | [optional] 
**python** | **str** | The path of the Python executable. Passenger uses Python to run the application.  **Note**:  The function only returns this value if you configure this application to use Python. | [optional] 
**ruby** | **str** | The path of the Ruby executable. Passenger uses Ruby to run the application.  **Note**:  The function only returns this value if you configure this application to use Ruby. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200371_result_data import InlineResponse200371ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200371ResultData from a JSON string
inline_response200371_result_data_instance = InlineResponse200371ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200371ResultData.to_json())

# convert the object into a dict
inline_response200371_result_data_dict = inline_response200371_result_data_instance.to_dict()
# create an instance of InlineResponse200371ResultData from a dict
inline_response200371_result_data_from_dict = InlineResponse200371ResultData.from_dict(inline_response200371_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



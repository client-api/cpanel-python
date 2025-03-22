# InlineResponse200470ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentroot** | **str** | The domain&#39;s absolute path to the directory&#39;s document root inside of the account&#39;s home directory. | [optional] 
**domain** | **str** | The domain name. | [optional] 
**homedir** | **str** | The absolute path to the cPanel account&#39;s home directory. | [optional] 
**serveralias** | **List[str]** | A list of the domain&#39;s aliases. | [optional] 
**template_settings** | [**InlineResponse200470ResultTemplateSettings**](InlineResponse200470ResultTemplateSettings.md) |  | [optional] 
**type** | **str** | The domain&#39;s type. * &#x60;main&#x60; — The main domain. * &#x60;sub&#x60; — A subdomain. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200470_result_data import InlineResponse200470ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200470ResultData from a JSON string
inline_response200470_result_data_instance = InlineResponse200470ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200470ResultData.to_json())

# convert the object into a dict
inline_response200470_result_data_dict = inline_response200470_result_data_instance.to_dict()
# create an instance of InlineResponse200470ResultData from a dict
inline_response200470_result_data_from_dict = InlineResponse200470ResultData.from_dict(inline_response200470_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



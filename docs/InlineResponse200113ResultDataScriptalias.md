# InlineResponse200113ResultDataScriptalias

An object containing CGI information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to the domain&#39;s CGI directory. | [optional] 
**url** | **str** | The domain&#39;s CGI directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200113_result_data_scriptalias import InlineResponse200113ResultDataScriptalias

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200113ResultDataScriptalias from a JSON string
inline_response200113_result_data_scriptalias_instance = InlineResponse200113ResultDataScriptalias.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200113ResultDataScriptalias.to_json())

# convert the object into a dict
inline_response200113_result_data_scriptalias_dict = inline_response200113_result_data_scriptalias_instance.to_dict()
# create an instance of InlineResponse200113ResultDataScriptalias from a dict
inline_response200113_result_data_scriptalias_from_dict = InlineResponse200113ResultDataScriptalias.from_dict(inline_response200113_result_data_scriptalias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



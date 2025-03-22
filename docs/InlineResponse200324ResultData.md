# InlineResponse200324ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirection_enabled** | **int** | Whether the domain redirects to another URL. * &#x60;1&#x60; - Redirects. * &#x60;0&#x60; - Doesn&#39;t redirect. | [optional] 
**url** | **str** | The URL to which to the domain redirects. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200324_result_data import InlineResponse200324ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200324ResultData from a JSON string
inline_response200324_result_data_instance = InlineResponse200324ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200324ResultData.to_json())

# convert the object into a dict
inline_response200324_result_data_dict = inline_response200324_result_data_instance.to_dict()
# create an instance of InlineResponse200324ResultData from a dict
inline_response200324_result_data_from_dict = InlineResponse200324ResultData.from_dict(inline_response200324_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



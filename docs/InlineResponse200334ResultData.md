# InlineResponse200334ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installed** | **int** | Whether ModSecurity is installed on the server. * &#x60;1&#x60; - Installed. * &#x60;0&#x60; - Not installed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200334_result_data import InlineResponse200334ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200334ResultData from a JSON string
inline_response200334_result_data_instance = InlineResponse200334ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200334ResultData.to_json())

# convert the object into a dict
inline_response200334_result_data_dict = inline_response200334_result_data_instance.to_dict()
# create an instance of InlineResponse200334ResultData from a dict
inline_response200334_result_data_from_dict = InlineResponse200334ResultData.from_dict(inline_response200334_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



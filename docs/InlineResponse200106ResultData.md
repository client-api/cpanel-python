# InlineResponse200106ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_name** | **str** | The authentication resource name. | [optional] 
**auth_type** | **str** | The directory&#39;s authentication type. * &#x60;Basic&#x60; * &#x60;None&#x60; | [optional] 
**passwd_file** | **str** | The path to the directory&#39;s password file. | [optional] 
**protected** | **int** | Whether the directory uses password protection. * &#x60;1&#x60; - Protected. * &#x60;0&#x60; - **Not** protected. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200106_result_data import InlineResponse200106ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200106ResultData from a JSON string
inline_response200106_result_data_instance = InlineResponse200106ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200106ResultData.to_json())

# convert the object into a dict
inline_response200106_result_data_dict = inline_response200106_result_data_instance.to_dict()
# create an instance of InlineResponse200106ResultData from a dict
inline_response200106_result_data_from_dict = InlineResponse200106ResultData.from_dict(inline_response200106_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



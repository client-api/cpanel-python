# InlineResponse200308ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dcv_file_allowed_characters** | **List[List[str]]** | An array that lists the characters which the provider allows in the DCV check file&#39;s filename. | [optional] 
**dcv_file_extension** | **str** | The DCV check file extension that the provider requires. | [optional] 
**dcv_file_random_character_count** | **int** | The number of characters that the provider allows in the DCV check file&#39;s filename. | [optional] 
**dcv_file_relative_path** | **str** | The path to the DCV check file, relative to the domain&#39;s document root directory. | [optional] 
**dcv_max_redirects** | **int** | The maximum number of HTTP redirects the provider allows. | [optional] 
**dcv_user_agent_string** | **str** | The user agent string that the system will use for the imitated local DCV check. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200308_result_data import InlineResponse200308ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200308ResultData from a JSON string
inline_response200308_result_data_instance = InlineResponse200308ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200308ResultData.to_json())

# convert the object into a dict
inline_response200308_result_data_dict = inline_response200308_result_data_instance.to_dict()
# create an instance of InlineResponse200308ResultData from a dict
inline_response200308_result_data_from_dict = InlineResponse200308ResultData.from_dict(inline_response200308_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



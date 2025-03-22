# InlineResponse200271ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** | Whether the function failed to create the thumbnail file.  **Note:**   * The function **only** returns this value if it doesn&#39;t create the thumbnail.  * &#x60;1&#x60; is the **only** possible value. | [optional] 
**file** | **str** | The file from which the function generated the thumbnail file. An absolute filepath. | [optional] 
**reason** | **str** | The reason that the function didn&#39;t create the thumbnail file.  **Note:**   The function only returns this value if it doesn&#39;t create the thumbnail. | [optional] 
**thumbnail_file** | **str** | The thumbnail file that the function generated. An absolute filepath. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200271_result_data import InlineResponse200271ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200271ResultData from a JSON string
inline_response200271_result_data_instance = InlineResponse200271ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200271ResultData.to_json())

# convert the object into a dict
inline_response200271_result_data_dict = inline_response200271_result_data_instance.to_dict()
# create an instance of InlineResponse200271ResultData from a dict
inline_response200271_result_data_from_dict = InlineResponse200271ResultData.from_dict(inline_response200271_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



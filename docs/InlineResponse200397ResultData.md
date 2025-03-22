# InlineResponse200397ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflict** | **int** | Whether a difference exists between the &#x60;type&#x60; and &#x60;onDiskType&#x60; returns. * &#x60;1&#x60; - Conflict exists. * &#x60;0&#x60; - **No** conflict exists. | [optional] 
**exists** | **int** | Whether the file exists in the user&#39;s directory or **only** in the backup. * &#x60;1&#x60; - File exists in the user&#39;s directory. * &#x60;0&#x60; - File exists **only** in the backup. | [optional] 
**name** | **str** | The name of the file or directory. | [optional] 
**on_disk_type** | **str** | The item type stored on the disk. * &#x60;dir&#x60; - A directory. * &#x60;file&#x60; - A file. * &#x60;symlink&#x60; - A symlink. * &#x60;unknown&#x60; - An unknown file type. | [optional] 
**type** | **str** | The item type stored in the backup. * &#x60;dir&#x60; - A directory. * &#x60;file&#x60; - A file. * &#x60;symlink&#x60; - A symlink. * &#x60;unknown&#x60; - An unknown file type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200397_result_data import InlineResponse200397ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200397ResultData from a JSON string
inline_response200397_result_data_instance = InlineResponse200397ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200397ResultData.to_json())

# convert the object into a dict
inline_response200397_result_data_dict = inline_response200397_result_data_instance.to_dict()
# create an instance of InlineResponse200397ResultData from a dict
inline_response200397_result_data_from_dict = InlineResponse200397ResultData.from_dict(inline_response200397_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



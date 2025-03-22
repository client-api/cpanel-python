# InlineResponse200399ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_date** | **str** | The date when the system created the backup. | [optional] 
**backup_id** | [**InlineResponse200399ResultDataBackupID**](InlineResponse200399ResultDataBackupID.md) |  | [optional] 
**backup_type** | **str** | The backup type.  * &#x60;compressed&#x60; —  A compressed tar file. * &#x60;incremental&#x60; — A full tree of files and directories. * &#x60;uncompressed&#x60; — An uncompressed tar file. | [optional] 
**exists** | **int** | Whether the item (a file, a directory, or a symlink) exists in the local disk or only in the backup.  * &#x60;1&#x60; — The item exists in the local disk. * &#x60;0&#x60; — The item exists only in the backup.  **Note:**  This return appears **only** if you set the &#x60;exists&#x60; parameter to &#x60;1&#x60;. | [optional] 
**file_size** | **int** | The size, in bytes, of the file in the backup.  **Note:**  The function returns this value **only** if the item is a file. | [optional] 
**mtime** | **int** | The file&#39;s last modification time. | [optional] 
**path** | **str** | The identical file path value that the system passed in the function. | [optional] 
**type** | **str** | The item type stored in the backup.  * &#x60;dir&#x60; — A directory. * &#x60;file&#x60; — A file. * &#x60;symlink&#x60; — A symlink. * &#x60;unknown&#x60; — An unknown file type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200399_result_data import InlineResponse200399ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200399ResultData from a JSON string
inline_response200399_result_data_instance = InlineResponse200399ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200399ResultData.to_json())

# convert the object into a dict
inline_response200399_result_data_dict = inline_response200399_result_data_instance.to_dict()
# create an instance of InlineResponse200399ResultData from a dict
inline_response200399_result_data_from_dict = InlineResponse200399ResultData.from_dict(inline_response200399_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



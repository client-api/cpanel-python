# InlineResponse200239ResultDataFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absdir** | **str** | The file path to the user&#39;s home directory. | [optional] 
**ctime** | **int** | The file&#39;s creation time. | [optional] 
**exists** | **int** | Whether the file exists in the directory.  * &#x60;1&#x60; — Exists. * &#x60;0&#x60; — Does **not** exist. | [optional] 
**file** | **str** | The filename. | [optional] 
**fullpath** | **str** | The file&#39;s full file path. | [optional] 
**gid** | **int** | The file owner&#39;s system group ID. | [optional] 
**hash** | **str** | The full file path&#39;s hash. | [optional] 
**humansize** | **str** | The formatted size of the file. The function returns the size with one of the following symbols:  * &#x60;KB&#x60; — Kilobytes. * &#x60;MB&#x60; — Megabytes. * &#x60;GB&#x60; — Gigabytes. | [optional] 
**isleaf** | **int** | Whether the directory contains subdirectories.  * &#x60;1&#x60; — Contains subdirectories. * &#x60;0&#x60; — Does **not** contain subdirectories. | [optional] 
**isparent** | **int** | Whether the file is a parent record.  * &#x60;1&#x60; — A parent record. * &#x60;0&#x60; — **Not** a parent record. | [optional] 
**mimename** | **str** | The file&#39;s MIME type name. | [optional] 
**mimetype** | **str** | The file&#39;s MIME type. | [optional] 
**mode** | **str** | The file&#39;s textual permissions. | [optional] 
**mtime** | **int** | The file&#39;s last modification time. | [optional] 
**nicemode** | **int** | The file&#39;s numerical permissions. | [optional] 
**path** | **str** | The absolute path to the file. | [optional] 
**phash** | **str** | The parent filepath&#39;s file hash. | [optional] 
**rawmimename** | **str** | The file&#39;s raw MIME type&#39;s name. | [optional] 
**rawmimetype** | **str** | The file&#39;s raw MIME type. | [optional] 
**read** | **int** | Whether the file is readable.  * &#x60;1&#x60; — Readable. * &#x60;0&#x60; — **Not** readable.  **Note:**  The function only returns this value if the &#x60;include_permissions&#x60; value is &#x60;1&#x60;. | [optional] 
**size** | **int** | The file&#39;s size, in bytes. | [optional] 
**type** | **str** | The item&#39;s type.  * &#x60;file&#x60; — A file. * &#x60;dir&#x60; — A directory. * &#x60;char&#x60; — A character special device. * &#x60;block&#x60; — A block special device. * &#x60;fifo&#x60; - A named pipe (FIFO). * &#x60;link&#x60; — A symbolic link. * &#x60;socket&#x60; — A Unix domain socket. | [optional] 
**uid** | **int** | The file owner&#39;s system user ID. | [optional] 
**write** | **int** | Whether the file is writable.  * &#x60;1&#x60; — Writable. * &#x60;0&#x60; — **Not** writable.  **Note:**  The function only returns this value if the &#x60;include_permissions&#x60; value is &#x60;1&#x60;. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200239_result_data_files import InlineResponse200239ResultDataFiles

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200239ResultDataFiles from a JSON string
inline_response200239_result_data_files_instance = InlineResponse200239ResultDataFiles.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200239ResultDataFiles.to_json())

# convert the object into a dict
inline_response200239_result_data_files_dict = inline_response200239_result_data_files_instance.to_dict()
# create an instance of InlineResponse200239ResultDataFiles from a dict
inline_response200239_result_data_files_from_dict = InlineResponse200239ResultDataFiles.from_dict(inline_response200239_result_data_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



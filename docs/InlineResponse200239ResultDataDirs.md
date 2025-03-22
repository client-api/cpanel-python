# InlineResponse200239ResultDataDirs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absdir** | **str** | The file path to the user&#39;s home directory. | [optional] 
**ctime** | **int** | The directory&#39;s creation date. | [optional] 
**exists** | **int** | Whether the directory exists in the directory.  * &#x60;1&#x60; — Exists. * &#x60;0&#x60; — Does **not** exist. | [optional] 
**file** | **str** | The directory name. | [optional] 
**fullpath** | **str** | The directory&#39;s full directory path. | [optional] 
**gid** | **int** | The directory owner&#39;s system group ID. | [optional] 
**hash** | **str** | The full directory path&#39;s hash. | [optional] 
**humansize** | **str** | The formatted size of the directory. The function returns the size with one of the following symbols:  * &#x60;KB&#x60; — Kilobytes. * &#x60;MB&#x60; — Megabytes. * &#x60;GB&#x60; — Gigabytes. | [optional] 
**isleaf** | **int** | Whether the directory contains subdirectories.  * &#x60;1&#x60; — Contains subdirectories. * &#x60;0&#x60; — Does **not** contain subdirectories. | [optional] 
**isparent** | **int** | Whether the directory is a parent record.  * &#x60;1&#x60; — A parent record. * &#x60;0&#x60; — **Not** a parent record. | [optional] 
**mimename** | **str** | The MIME type&#39;s name. | [optional] 
**mimetype** | **str** | The directory&#39;s MIME&#39;s type. | [optional] 
**mode** | **str** | The directory&#39;s textual permissions in [Unix format](http://en.wikipedia.org/wiki/File_system_permissions#Notation_of_traditional_Unix_permissions). | [optional] 
**mtime** | **int** | The directory&#39;s last modification time. | [optional] 
**nicemode** | **int** | The directory&#39;s numerical permissions. | [optional] 
**path** | **str** | The path to the directory. | [optional] 
**phash** | **str** | The parent directory path&#39;s hash. | [optional] 
**rawmimename** | **str** | The directory&#39;s raw MIME type&#39;s name. | [optional] 
**rawmimetype** | **str** | The directory&#39;s raw MIME type. | [optional] 
**read** | **int** | Whether the directory is readable.  * &#x60;1&#x60; — Readable. * &#x60;0&#x60; — **Not** readable.  **Note:**  The function only returns this value if the &#x60;include_permissions&#x60; value is &#x60;1&#x60;. | [optional] 
**size** | **int** | The directory&#39;s size, in bytes. | [optional] 
**type** | **str** | The item&#39;s type.  * &#x60;file&#x60; — A file. * &#x60;dir&#x60; — A directory. * &#x60;char&#x60; — A character special device. * &#x60;block&#x60; — A block special device. * &#x60;fifo&#x60; - A named pipe (FIFO). * &#x60;link&#x60; — A symbolic link. * &#x60;socket&#x60; — A Unix domain socket. | [optional] 
**uid** | **int** | The directory owner&#39;s system user ID. | [optional] 
**write** | **int** | Whether the directory is writable.  * &#x60;1&#x60; — Writable. * &#x60;0&#x60; — **Not** writable.  **Note:**  The function only returns this value if the &#x60;include_permissions&#x60; value is &#x60;1&#x60;. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200239_result_data_dirs import InlineResponse200239ResultDataDirs

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200239ResultDataDirs from a JSON string
inline_response200239_result_data_dirs_instance = InlineResponse200239ResultDataDirs.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200239ResultDataDirs.to_json())

# convert the object into a dict
inline_response200239_result_data_dirs_dict = inline_response200239_result_data_dirs_instance.to_dict()
# create an instance of InlineResponse200239ResultDataDirs from a dict
inline_response200239_result_data_dirs_from_dict = InlineResponse200239ResultDataDirs.from_dict(inline_response200239_result_data_dirs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



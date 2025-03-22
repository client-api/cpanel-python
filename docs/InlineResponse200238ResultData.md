# InlineResponse200238ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absdir** | **str** | The path to the user&#39;s home directory. | [optional] 
**ctime** | **int** | The file&#39;s creation time, Unix time format. | [optional] 
**exists** | **int** | Whether the file exists in the directory. * &#x60;1&#x60; - Exists. * &#x60;0&#x60; - Does **not** exist. | [optional] 
**file** | **str** | The filename. | [optional] 
**fullpath** | **str** | The file&#39;s full filepath. | [optional] 
**gid** | **int** | The file owner&#39;s system group ID. | [optional] 
**hash** | **str** | The full filepath&#39;s hash. | [optional] 
**humansize** | **str** | The file&#39;s formatted size, followed by one of the following symbols: * &#x60;KB&#x60; - kilobytes * &#x60;MB&#x60; - megabytes * &#x60;GB&#x60; - gigabytes | [optional] 
**isleaf** | **int** | Whether the directory contains subdirectories. * &#x60;1&#x60; - Contains subdirectories. * &#x60;0&#x60; - Does **not** contain subdirectories. | [optional] 
**mimename** | **str** | The file&#39;s MIME name. | [optional] 
**mimetype** | **str** | The file&#39;s MIME type. | [optional] 
**mode** | **str** | The file&#39;s textual permissions in [Unix format](https://en.wikipedia.org/wiki/File-system_permissions#Notation_of_traditional_Unix_permissions). | [optional] 
**mtime** | **int** | The file&#39;s last modification time, in Unix time format. | [optional] 
**nicemode** | **int** | The file&#39;s numerical permissions in [octal notation](https://en.wikipedia.org/wiki/File-system_permissions#Notation_of_traditional_Unix_permissions). | [optional] 
**path** | **str** | The file&#39;s path. | [optional] 
**phash** | **str** | The parent filepath&#39;s file hash. | [optional] 
**rawmimename** | **str** | The file&#39;s raw MIME name. | [optional] 
**rawmimetype** | **str** | The file&#39;s raw MIME type. | [optional] 
**read** | **int** | Whether the file is readable. The function only returns this value if you set the &#x60;include_permissions&#x60; value to 1. * &#x60;1&#x60; - Readable. * &#x60;0&#x60; - **Not** readable. | [optional] 
**size** | **int** | The file&#39;s size, in bytes. | [optional] 
**type** | **str** | The item&#39;s type. * &#x60;file&#x60; - File. * &#x60;dir&#x60; - Directory. * &#x60;char&#x60; - Character special device. * &#x60;block&#x60; - Block special device. * &#x60;fifo&#x60; - Named pipe. * &#x60;link&#x60; - Symbolic link. * &#x60;socket&#x60; - Unix domain socket. | [optional] 
**uid** | **int** | The file owner&#39;s system user ID. | [optional] 
**write** | **int** | Whether the file is writable. The function only returns this value if you set the &#x60;include_permissions&#x60; value to 1 . * &#x60;1&#x60; - Writable. * &#x60;0&#x60; - Not writable. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200238_result_data import InlineResponse200238ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200238ResultData from a JSON string
inline_response200238_result_data_instance = InlineResponse200238ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200238ResultData.to_json())

# convert the object into a dict
inline_response200238_result_data_dict = inline_response200238_result_data_instance.to_dict()
# create an instance of InlineResponse200238ResultData from a dict
inline_response200238_result_data_from_dict = InlineResponse200238ResultData.from_dict(inline_response200238_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



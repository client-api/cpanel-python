# InlineResponse200128ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **int** | The directory depth of the item&#39;s path. | [optional] 
**file** | **str** | The item&#39;s base name. | [optional] 
**fullpath** | **str** | The item&#39;s absolute path. | [optional] 
**isleaf** | **int** | Whether the item is a file or a directory. * &#x60;1&#x60; - File. * &#x60;0&#x60; - Directory. | [optional] 
**ismailbox** | **int** | Whether the item is a mailbox. * &#x60;1&#x60; - Mailbox. * &#x60;0&#x60; - **Not** a mailbox. | [optional] 
**mtime** | **int** | The item&#39;s modification time. A time, in [Unix time](https://en.wikipedia.org/wiki/Unix_time) format. | [optional] 
**path** | **str** | The item&#39;s directory&#39;s path. | [optional] 
**relpath** | **str** | The item&#39;s relative path. | [optional] 
**type** | **str** | The item type. * &#x60;dir&#x60; - The item is a directory. * &#x60;file&#x60; - The item is a file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200128_result_data import InlineResponse200128ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200128ResultData from a JSON string
inline_response200128_result_data_instance = InlineResponse200128ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200128ResultData.to_json())

# convert the object into a dict
inline_response200128_result_data_dict = inline_response200128_result_data_instance.to_dict()
# create an instance of InlineResponse200128ResultData from a dict
inline_response200128_result_data_from_dict = InlineResponse200128ResultData.from_dict(inline_response200128_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200393ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**byte_limit** | **int** | The limit for disk space the cPanel account may use on this server, in bytes. * A positive integer. * &#x60;0&#x60; - Unlimited or disabled server quotas.  **Note:**   This value does **not** update immediately. | [optional] 
**bytes_used** | **int** | The amount of disk space the cPanel account uses on this server, in bytes. * A positive integer. * &#x60;0&#x60; - No usage or disabled server quotas. | [optional] 
**inode_limit** | **int** | The limit for inodes that the cPanel account may use on this server. * A positive integer. * &#x60;0&#x60; - Unlimited or disabled server quotas. | [optional] 
**inodes_used** | **int** | The number of inodes that the cPanel account uses on this server. * A positive integer. * &#x60;0&#x60; - No usage or disabled server quotas. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200393_result_data import InlineResponse200393ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200393ResultData from a JSON string
inline_response200393_result_data_instance = InlineResponse200393ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200393ResultData.to_json())

# convert the object into a dict
inline_response200393_result_data_dict = inline_response200393_result_data_instance.to_dict()
# create an instance of InlineResponse200393ResultData from a dict
inline_response200393_result_data_from_dict = InlineResponse200393ResultData.from_dict(inline_response200393_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



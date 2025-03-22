# InlineResponse200394ResultData

An object containing the cPanel account's quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inode_limit** | [**InlineResponse200394ResultDataInodeLimit**](InlineResponse200394ResultDataInodeLimit.md) |  | [optional] 
**inodes_remain** | [**InlineResponse200394ResultDataInodesRemain**](InlineResponse200394ResultDataInodesRemain.md) |  | [optional] 
**inodes_used** | [**InlineResponse200394ResultDataInodesUsed**](InlineResponse200394ResultDataInodesUsed.md) |  | [optional] 
**megabyte_limit** | [**InlineResponse200394ResultDataMegabyteLimit**](InlineResponse200394ResultDataMegabyteLimit.md) |  | [optional] 
**megabytes_remain** | [**InlineResponse200394ResultDataMegabytesRemain**](InlineResponse200394ResultDataMegabytesRemain.md) |  | [optional] 
**megabytes_used** | [**InlineResponse200394ResultDataMegabytesUsed**](InlineResponse200394ResultDataMegabytesUsed.md) |  | [optional] 
**under_inode_limit** | **int** | Whether the account is under its inode limit.  * &#x60;1&#x60; — Under limit. * &#x60;0&#x60; — Over limit. | [optional] 
**under_megabyte_limit** | **int** | Whether the account is under its disk space limit, in megabytes (MB).  * &#x60;1&#x60; — Under limit. * &#x60;0&#x60; — Over limit. | [optional] 
**under_quota_overall** | **int** | Whether the account is under both its inode and disk megabyte (MB) limit.  * &#x60;1&#x60; — Under limit. * &#x60;0&#x60; — Over limit. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200394_result_data import InlineResponse200394ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200394ResultData from a JSON string
inline_response200394_result_data_instance = InlineResponse200394ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200394ResultData.to_json())

# convert the object into a dict
inline_response200394_result_data_dict = inline_response200394_result_data_instance.to_dict()
# create an instance of InlineResponse200394ResultData from a dict
inline_response200394_result_data_from_dict = InlineResponse200394ResultData.from_dict(inline_response200394_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



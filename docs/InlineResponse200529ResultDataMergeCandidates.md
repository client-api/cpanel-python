# InlineResponse200529ResultDataMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_email** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**can_delete** | **int** |  | [optional] 
**can_set_password** | **int** |  | [optional] 
**can_set_quota** | **int** |  | [optional] 
**dismissed** | **int** |  | [optional] 
**dismissed_merge_candidates** | **List[str]** |  | [optional] 
**domain** | **str** |  | [optional] 
**full_username** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**has_expired_invite** | **int** |  | [optional] 
**has_invite** | **int** |  | [optional] 
**has_siblings** | **int** |  | [optional] 
**invite_expiration** | **int** |  | [optional] 
**issues** | **List[str]** |  | [optional] 
**merge_candidates** | **List[str]** |  | [optional] 
**parent_type** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**real_name** | **str** |  | [optional] 
**services** | **object** |  | [optional] 
**special** | **int** |  | [optional] 
**sub_account_exists** | **int** |  | [optional] 
**synced_password** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data_merge_candidates import InlineResponse200529ResultDataMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultDataMergeCandidates from a JSON string
inline_response200529_result_data_merge_candidates_instance = InlineResponse200529ResultDataMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultDataMergeCandidates.to_json())

# convert the object into a dict
inline_response200529_result_data_merge_candidates_dict = inline_response200529_result_data_merge_candidates_instance.to_dict()
# create an instance of InlineResponse200529ResultDataMergeCandidates from a dict
inline_response200529_result_data_merge_candidates_from_dict = InlineResponse200529ResultDataMergeCandidates.from_dict(inline_response200529_result_data_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



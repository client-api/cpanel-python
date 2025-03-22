# SubaccountMergeCandidatesEmpty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_candidates** | **List[object]** | An array of objects that represents the service accounts that the system could merge for this subaccount. | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_merge_candidates_empty import SubaccountMergeCandidatesEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountMergeCandidatesEmpty from a JSON string
subaccount_merge_candidates_empty_instance = SubaccountMergeCandidatesEmpty.from_json(json)
# print the JSON string representation of the object
print(SubaccountMergeCandidatesEmpty.to_json())

# convert the object into a dict
subaccount_merge_candidates_empty_dict = subaccount_merge_candidates_empty_instance.to_dict()
# create an instance of SubaccountMergeCandidatesEmpty from a dict
subaccount_merge_candidates_empty_from_dict = SubaccountMergeCandidatesEmpty.from_dict(subaccount_merge_candidates_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



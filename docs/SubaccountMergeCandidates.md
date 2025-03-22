# SubaccountMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_candidates** | [**List[SubaccountMergeCandidatesMergeCandidatesInner]**](SubaccountMergeCandidatesMergeCandidatesInner.md) | An array of objects that represents the service accounts that the system could merge for this subaccount. | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_merge_candidates import SubaccountMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountMergeCandidates from a JSON string
subaccount_merge_candidates_instance = SubaccountMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(SubaccountMergeCandidates.to_json())

# convert the object into a dict
subaccount_merge_candidates_dict = subaccount_merge_candidates_instance.to_dict()
# create an instance of SubaccountMergeCandidates from a dict
subaccount_merge_candidates_from_dict = SubaccountMergeCandidates.from_dict(subaccount_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



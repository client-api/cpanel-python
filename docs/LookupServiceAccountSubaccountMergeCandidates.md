# LookupServiceAccountSubaccountMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_candidates** | [**List[LookupServiceAccountSubaccountMergeCandidatesMergeCandidatesInner]**](LookupServiceAccountSubaccountMergeCandidatesMergeCandidatesInner.md) | An array of objects that represents the service accounts that the system could merge for this subaccount. | [optional] 

## Example

```python
from clientapi_cpanel.models.lookup_service_account_subaccount_merge_candidates import LookupServiceAccountSubaccountMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of LookupServiceAccountSubaccountMergeCandidates from a JSON string
lookup_service_account_subaccount_merge_candidates_instance = LookupServiceAccountSubaccountMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(LookupServiceAccountSubaccountMergeCandidates.to_json())

# convert the object into a dict
lookup_service_account_subaccount_merge_candidates_dict = lookup_service_account_subaccount_merge_candidates_instance.to_dict()
# create an instance of LookupServiceAccountSubaccountMergeCandidates from a dict
lookup_service_account_subaccount_merge_candidates_from_dict = LookupServiceAccountSubaccountMergeCandidates.from_dict(lookup_service_account_subaccount_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



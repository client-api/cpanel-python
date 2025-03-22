# LookupServiceAccountSubaccountMergeCandidatesEmpty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_candidates** | **List[object]** | An array of objects that represents the service accounts that the system could merge for this subaccount. | [optional] 

## Example

```python
from clientapi_cpanel.models.lookup_service_account_subaccount_merge_candidates_empty import LookupServiceAccountSubaccountMergeCandidatesEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of LookupServiceAccountSubaccountMergeCandidatesEmpty from a JSON string
lookup_service_account_subaccount_merge_candidates_empty_instance = LookupServiceAccountSubaccountMergeCandidatesEmpty.from_json(json)
# print the JSON string representation of the object
print(LookupServiceAccountSubaccountMergeCandidatesEmpty.to_json())

# convert the object into a dict
lookup_service_account_subaccount_merge_candidates_empty_dict = lookup_service_account_subaccount_merge_candidates_empty_instance.to_dict()
# create an instance of LookupServiceAccountSubaccountMergeCandidatesEmpty from a dict
lookup_service_account_subaccount_merge_candidates_empty_from_dict = LookupServiceAccountSubaccountMergeCandidatesEmpty.from_dict(lookup_service_account_subaccount_merge_candidates_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200527ResultDataAccounts

An object containing the service accounts that match the queried `full_username` parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_email** | **str** | An alternate email address for the Subaccount&#39;s user. | [optional] 
**avatar_url** | **str** | The URL to the user&#39;s Subaccount profile image file. | [optional] 
**can_delete** | **int** | Whether the cPanel account user can delete the Subaccount.  * &#x60;1&#x60; — Can delete. * &#x60;0&#x60; — **Cannot** delete. | [optional] 
**can_set_password** | **int** | Whether the cPanel account user can change the Subaccount&#39;s password.  * &#x60;1&#x60; — Can change the password. * &#x60;0&#x60; — **Cannot** change the password.  **Note:**  the function returns &#x60;0&#x60; for Subaccounts that inherit their password from the cPanel account. | [optional] 
**can_set_quota** | **int** | Whether the cPanel account user can change the Subaccount&#39;s disk usage quota.  * &#x60;1&#x60; — Can change the Subaccount&#39;s disk usage quota. * &#x60;0&#x60; — **Cannot** change the Subaccount&#39;s disk useage quota. | [optional] 
**dismissed** | **int** | Whether the cPanel account user dismissed the merge prompt for the service account.  * &#x60;1&#x60; — Dismissed. * &#x60;0&#x60; — Did **not** dismiss.  **Note:**  **Only** service accounts return this value. | [optional] 
**dismissed_merge_candidates** | **List[str]** | A list of the service accounts that the user dismissed the merge prompt for.  **Note:**  * This array **always** returns empty. * We reserved this return for future use. | [optional] 
**domain** | **str** | The Subaccount user&#39;s associated domain. | [optional] 
**full_username** | **str** | The Subaccount&#39;s username. | [optional] 
**guid** | **str** | The Subaccount&#39;s system-assigned unique identifier. | [optional] 
**has_expired_invite** | **int** | Whether the Subaccount owns an expired invitation.  * &#x60;1&#x60; — Owns an expired invitation. * &#x60;0&#x60; — Does **not** own an expired invitation. | [optional] 
**has_invite** | **int** | Whether the Subaccount owns an active invitation.  * &#x60;1&#x60; — Own an active invitation. * &#x60;0&#x60; — Does **not** own an active invitation. | [optional] 
**has_siblings** | **int** | Whether the service account shares the queried &#x60;full_username&#x60; value with another service account.  * &#x60;1&#x60; — Shares the service account. * &#x60;0&#x60; — Does **not** share the service account. | [optional] 
**invite_expiration** | **int** | The time at which the new Subaccount invitation will expire.  * &#x60;null&#x60; — The account does **not** own an active invitation. | [optional] 
**issues** | [**List[InlineResponse200527ResultDataAccountsIssues]**](InlineResponse200527ResultDataAccountsIssues.md) | An array of objects containing information about any issues or problems with the Subaccount. | [optional] 
**merge_candidates** | [**List[InlineResponse200527ResultDataAccountsMergeCandidates]**](InlineResponse200527ResultDataAccountsMergeCandidates.md) | An array of objects containing the service accounts that the system could merge for this Subaccount. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts import InlineResponse200527ResultDataAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccounts from a JSON string
inline_response200527_result_data_accounts_instance = InlineResponse200527ResultDataAccounts.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccounts.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_dict = inline_response200527_result_data_accounts_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccounts from a dict
inline_response200527_result_data_accounts_from_dict = InlineResponse200527ResultDataAccounts.from_dict(inline_response200527_result_data_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



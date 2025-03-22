# InlineResponse200527ResultDataAccountsMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_type** | **str** | The type of account that could own the service account.  * &#x60;sub&#x60; — A Subaccount. * &#x60;hypothetical&#x60; — A hypothetical Subaccount that does **not** yet exist, but that the user could create as part of a merge. * &#x60;null&#x60; — **Not** a merge candidate. | [optional] 
**phone_number** | **str** | The Subaccount user&#39;s phone number, in [ITU-T-recommended E.164](https://en.wikipedia.org/wiki/E.164) format. | [optional] 
**real_name** | **str** | The name of the Subaccount user, if provided. | [optional] 
**services** | [**InlineResponse200527ResultDataAccountsServices**](InlineResponse200527ResultDataAccountsServices.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user **cannot** remove.  * &#x60;1&#x60; — The user can remove the account. * &#x60;0&#x60; — The user **cannot** remove the account. | [optional] 
**sub_account_exists** | **int** | Whether a Subaccount exists with the same username.  * &#x60;1&#x60; — Exists. * &#x60;0&#x60; — Does **not** exist. * &#x60;null&#x60; — The account is **not** a Subaccount. | [optional] 
**synced_password** | **int** | Whether the user has synchronized the passwords for each of the Subaccount&#39;s service accounts.  * &#x60;1&#x60; — Synchronized. * &#x60;0&#x60; — **Not** synchronized. * &#x60;null&#x60; — The account is **not** a Subaccount. | [optional] 
**type** | **str** | The type of account.  * &#x60;sub&#x60; — A Subaccount. * &#x60;hypothetical&#x60; — A hypothetical Subaccount that does **not** yet exist, but that the user could create as part of a merge. * &#x60;service&#x60; — A service account. * &#x60;cpanel&#x60; — A cPanel account. | [optional] 
**username** | **str** | The username for the Subaccount.  **Note:**  This value does **not** include the domain name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts_merge_candidates import InlineResponse200527ResultDataAccountsMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccountsMergeCandidates from a JSON string
inline_response200527_result_data_accounts_merge_candidates_instance = InlineResponse200527ResultDataAccountsMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccountsMergeCandidates.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_merge_candidates_dict = inline_response200527_result_data_accounts_merge_candidates_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccountsMergeCandidates from a dict
inline_response200527_result_data_accounts_merge_candidates_from_dict = InlineResponse200527ResultDataAccountsMergeCandidates.from_dict(inline_response200527_result_data_accounts_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



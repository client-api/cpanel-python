# InlineResponse200535ResultDataMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_email** | **str** | An alternate email address for the subaccount&#39;s user. | [optional] 
**avatar_url** | **str** | The user&#39;s subaccount profile photo. | [optional] 
**can_delete** | **int** | Whether the cPanel account user can delete the subaccount. * &#x60;1&#x60; - Can delete. * &#x60;0&#x60; - **Cannot** delete. | [optional] 
**can_set_password** | **int** | Whether the cPanel account user can change the subaccount&#39;s password. * &#x60;1&#x60; - Can change. * &#x60;0&#x60; - **Cannot** change.  **Note:**  The function returns a &#x60;0&#x60; value for subaccounts that inherit their password from the cPanel account. | [optional] 
**can_set_quota** | **int** | Whether the cPanel account user can change the subaccount&#39;s disk usage quota. * &#x60;1&#x60; - Can change. * &#x60;0&#x60; - **Cannot** change. | [optional] 
**domain** | **str** | The subaccount user&#39;s associated domain. A domain that the cPanel account owns. | [optional] 
**full_username** | **str** | The subaccount&#39;s username and domain name. | [optional] 
**guid** | **str** | The subaccount unique identifier. The system assigned unique value. | [optional] 
**has_siblings** | **int** | Whether the service account shares a &#x60;full_username&#x60; value with another service account. * &#x60;1&#x60; - Shares. * &#x60;0&#x60; - Does **not** share. | [optional] 
**issues** | [**List[InlineResponse200535ResultDataIssues]**](InlineResponse200535ResultDataIssues.md) | Information about any issues or problems with the subaccount. | [optional] 
**parent_type** | **str** | The type of account that could own the service account. * &#x60;sub&#x60; - A subaccount. * &#x60;hypothetical&#x60; - A hypothetical subaccount that does **not** yet exist, but the user could create as part of a merge. * &#x60;null&#x60; - Not a merge candidate. | [optional] 
**phone_number** | **str** | The subaccount user&#39;s phone number. | [optional] 
**real_name** | **str** | The name of the subaccount&#39;s user.  * A first name. * Last name. * First name and last name. * An empty string. | [optional] 
**services** | [**InlineResponse200535ResultDataServices1**](InlineResponse200535ResultDataServices1.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user **cannot** remove. * &#x60;1&#x60; - A special account. * &#x60;0&#x60; - **Not** a special account. | [optional] 
**sub_account_exists** | **int** | Whether a subaccount exists with the same username.  * &#x60;1&#x60; - Exists. * &#x60;0&#x60; - Does **not** exist.  **Note:**  The function returns a &#x60;null&#x60; value if the account is **not** a service account. | [optional] 
**synced_password** | **int** | Whether the user has synchronized the passwords for each of the subaccount&#39;s service accounts.  * &#x60;1&#x60; - Synchronized. * &#x60;0&#x60; - **Not** synchronized.  **Note:**  The function returns a &#x60;null&#x60; value if the account is **not** a subaccount. | [optional] 
**type** | **str** | The type of account.  * &#x60;sub&#x60; - A subaccount. * &#x60;hypothetical&#x60; - A hypothetical subaccount that does **not** exist, but that the user could create as part of a merge. * &#x60;service&#x60; - A service account. * &#x60;cpanel&#x60; - The cPanel account. | [optional] 
**username** | **str** | The username for the service account that meets the account name limitations.  * Length - 64 characters * Characters — &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, dot (&#x60;.&#x60;), hyphen (&#x60;-&#x60;), underscore (&#x60;_&#x60;).  **Note:**  This value does **not** include the domain name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200535_result_data_merge_candidates import InlineResponse200535ResultDataMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200535ResultDataMergeCandidates from a JSON string
inline_response200535_result_data_merge_candidates_instance = InlineResponse200535ResultDataMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200535ResultDataMergeCandidates.to_json())

# convert the object into a dict
inline_response200535_result_data_merge_candidates_dict = inline_response200535_result_data_merge_candidates_instance.to_dict()
# create an instance of InlineResponse200535ResultDataMergeCandidates from a dict
inline_response200535_result_data_merge_candidates_from_dict = InlineResponse200535ResultDataMergeCandidates.from_dict(inline_response200535_result_data_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



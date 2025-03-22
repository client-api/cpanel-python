# InlineResponse200529ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_email** | **str** | An alternate email address for the account&#39;s user. | [optional] 
**avatar_url** | **str** | The user&#39;s account profile photo.  The URL must point to an image file. | [optional] 
**can_delete** | **int** | Whether the cPanel account user can delete the account. * &#x60;1&#x60; - Can delete. * &#x60;0&#x60; - **Cannot** delete. | [optional] 
**can_set_password** | **int** | Whether the cPanel account user can change the account&#39;s password. * &#x60;1&#x60; - Can change password. * &#x60;0&#x60; - **Cannot** change password.  **Note:**  The function returns &#x60;0&#x60; for accounts that inherit their password from the cPanel account. | [optional] 
**can_set_quota** | **int** | Whether the cPanel account user can change the account&#39;s disk usage quota. * &#x60;1&#x60; - Can change quota. * &#x60;0&#x60; - **Cannot** change quota. | [optional] 
**dismissed** | **int** | Whether the cPanel account user dismissed the merge prompt for the service account. * &#x60;1&#x60; - Dismissed prompt. * &#x60;0&#x60; - Did **not** dismiss prompt.  **Note:**  **Only** service accounts return this value. | [optional] 
**dismissed_merge_candidates** | **List[object]** | An array of objects that represent the service accounts that the user dismissed the merge prompt for. This array will always return empty.  **Note:**  We reserved this return for future use. | [optional] 
**domain** | **str** | The account user&#39;s associated domain. | [optional] 
**full_username** | **str** | The account&#39;s username and domain name, separated by the &#x60;@&#x60; character. | [optional] 
**guid** | **str** | The account unique identifier. | [optional] 
**has_expired_invite** | **int** | Whether the Subaccount owns an expired invitation. * &#x60;1&#x60; - Owns an expired invitation. * &#x60;0&#x60; - Does **not** own an expired invitation. | [optional] 
**has_invite** | **int** | Whether the Subaccount owns an active invitation. * &#x60;1&#x60; - Owns an invitation. * &#x60;0&#x60; - Does **not** own an invitation. | [optional] 
**has_siblings** | **int** | Whether the service account shares a &#x60;full_username&#x60; value with another service account. * &#x60;1&#x60; - Shares. * &#x60;0&#x60; - Does not share. | [optional] 
**invite_expiration** | **int** | The time at which the new Subaccount invitation will expire, given as a valid Unix epoch time or null.  If the account does not own an active invitation, this value returns &#x60;null&#x60;. | [optional] 
**issues** | [**List[InlineResponse200529ResultDataIssues]**](InlineResponse200529ResultDataIssues.md) | Information about any issues or problems with the account. | [optional] 
**merge_candidates** | [**List[InlineResponse200529ResultDataMergeCandidates]**](InlineResponse200529ResultDataMergeCandidates.md) | The service accounts that the system could merge for this account.  **Note:**  You can find descriptions for this array&#39;s returns within this table. | [optional] 
**parent_type** | **str** | The type of account that could own the service account. * &#x60;sub&#x60; - An account. * &#x60;hypothetical&#x60; - A hypothetical account does **not** yet exist, but that the user could create as part of a merge. * &#x60;null&#x60; - **Not** a merge candidate. | [optional] 
**phone_number** | **str** | The account user&#39;s phone number. * A valid phone number that conforms to [ITU-T](https://en.wikipedia.org/wiki/ITU-T)&#39;s [E.164-recommended standard](https://en.wikipedia.org/wiki/E.164) for the representation of telephone numbers. | [optional] 
**real_name** | **str** | The name of the account&#39;s user. * A first name, a last name, or a first name and last name. * An empty string. | [optional] 
**services** | [**InlineResponse200529ResultDataServices**](InlineResponse200529ResultDataServices.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user **cannot** remove. * &#x60;1&#x60; - A special account. * &#x60;0&#x60; - **Not** a special account. | [optional] 
**sub_account_exists** | **int** | Whether an account exists with the same username. * &#x60;1&#x60; - Exists. * &#x60;0&#x60; - Does not exist. * &#x60;null&#x60; - The account is **not** a service account. | [optional] 
**synced_password** | **int** | Whether the user has synchronized the passwords for each of the account&#39;s service accounts. * &#x60;1&#x60; - Synchronized. * &#x60;0&#x60; - **Not** synchronized. * &#x60;null&#x60; - The account is **not** a Subaccount | [optional] 
**type** | **str** | The type of account. * &#x60;hypothetical&#x60; - A hypothetical account that does not exist, but that the user could create as part of a merge. * &#x60;service&#x60; - A service account. | [optional] 
**username** | **str** | The account username.  The username must meet the account name limitations. * Characters - &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, dot (&#x60;.&#x60;), hyphen (&#x60;-&#x60;), underscore (&#x60;_&#x60;)  **Note::**  This value does **not** include the domain name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data import InlineResponse200529ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultData from a JSON string
inline_response200529_result_data_instance = InlineResponse200529ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultData.to_json())

# convert the object into a dict
inline_response200529_result_data_dict = inline_response200529_result_data_instance.to_dict()
# create an instance of InlineResponse200529ResultData from a dict
inline_response200529_result_data_from_dict = InlineResponse200529ResultData.from_dict(inline_response200529_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SubaccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_email** | **str** | An alternate email address for the subaccount&#39;s user. | [optional] 
**avatar_url** | **str** | The HTTPS URL to the user&#39;s subaccount profile photo image file. | [optional] 
**can_delete** | **int** | Whether the cPanel account user can delete the subaccount. * &#x60;1&#x60; - Can delete. * &#x60;0&#x60; - **Cannot** delete. | [optional] 
**can_set_password** | **int** | Whether the cPanel account user can change the subaccount&#39;s password. * &#x60;1&#x60; - Can change. * &#x60;0&#x60; - **Cannot** change.  **Note:**    The function returns a &#x60;0&#x60; value for subaccounts that inherit their password from the cPanel account. | [optional] 
**can_set_quota** | **int** | Whether the cPanel account user can change the subaccount&#39;s disk usage quota. * &#x60;1&#x60; - Can change. * &#x60;0&#x60; - **Cannot** change. | [optional] 
**dismissed** | **int** | Whether the cPanel account user dismissed the merge prompt for the service account.  * &#x60;1&#x60; - Dismissed. * &#x60;0&#x60; - Did **not** dismiss.  **Note:**  **Only** service accounts return this value. | [optional] 
**domain** | **str** | The subaccount user&#39;s associated domain. | [optional] 
**full_username** | **str** | The subaccount&#39;s username and domain name. | [optional] 
**guid** | **str** | The subaccount unique identifier. | [optional] 
**has_siblings** | **int** | Whether the service account shares a &#x60;full_username&#x60; value with another service account. * &#x60;1&#x60; - Shares. * &#x60;0&#x60; - Does **not** share. | [optional] 
**issues** | [**List[SubaccountBaseIssues]**](SubaccountBaseIssues.md) | Information about any issues or problems with the subaccount. | [optional] 
**parent_type** | **str** | The type of account that could own the service account. * &#x60;sub&#x60; - A subaccount. * &#x60;hypothetical&#x60; - A hypothetical subaccount that does **not** yet exist, but the user could create as part of a merge. * &#x60;null&#x60; - **Not** a merge candidate. | [optional] 
**phone_number** | **str** | The subaccount user&#39;s phone number. A valid phone number that conforms to [ITU-T](https://en.wikipedia.org/wiki/ITU-T)&#39;s [E.164](https://en.wikipedia.org/wiki/E.164)-recommended standard for the representation of telephone numbers. | [optional] 
**real_name** | **str** | The name of the subaccount&#39;s user, if provided. | [optional] 
**services** | [**SubaccountBaseServices**](SubaccountBaseServices.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user **cannot** remove. * &#x60;1&#x60; - A special account. * &#x60;0&#x60; - **Not** a special account. | [optional] 
**sub_account_exists** | **int** | Whether a subaccount exists with the same username. * &#x60;1&#x60; - Exists. * &#x60;0&#x60; - Does not exist.  **Note:**  The function returns a null value if the account is **not** a service account. | [optional] 
**synced_password** | **int** | Whether the user has synchronized the passwords for each of the subaccount&#39;s service accounts. * &#x60;1&#x60; - Synchronized. * &#x60;0&#x60; - **Not** synchronized.  **Note:**  The function returns a null value if the account is **not** a subaccount. | [optional] 
**type** | **str** | The type of account. * &#x60;sub&#x60; - A subaccount. * &#x60;hypothetical&#x60; - A hypothetical subaccount that does not exist, but that the user could create as part of a merge. * &#x60;service&#x60; - A service account. * &#x60;cpanel&#x60; - The cPanel account. | [optional] 
**username** | **str** | The subaccount&#39;s username. | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_base import SubaccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBase from a JSON string
subaccount_base_instance = SubaccountBase.from_json(json)
# print the JSON string representation of the object
print(SubaccountBase.to_json())

# convert the object into a dict
subaccount_base_dict = subaccount_base_instance.to_dict()
# create an instance of SubaccountBase from a dict
subaccount_base_from_dict = SubaccountBase.from_dict(subaccount_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



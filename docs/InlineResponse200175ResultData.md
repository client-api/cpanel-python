# InlineResponse200175ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpuser_spam_auto_delete** | **int** | The cPanel user&#39;s account-wide spam filter setting  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled.  **NOTE:**  This key **only** appears if the &#x60;account&#x60; parameter is passed **and** the account does **not** have a custom setting | [optional] 
**cpuser_spam_auto_delete_score** | **int** | The cPanel user&#39;s account-wide spam filter threshold score. For more information, see &#x60;Email::add_spam_filter&#x60;.  **NOTE:**  This key **only** appears if the &#x60;account&#x60; parameter is passed **and** the account does **not** have a custom setting | [optional] 
**rewrites_subjects** | **int** | Whether the user&#39;s spam filter rewrites the subject lines of spam messages.  * &#x60;1&#x60; -  Rewrite. * &#x60;0&#x60; -  No rewrites. | [optional] 
**spam_as_acl** | **int** | Whether the user&#39;s spam filter uses Apache SpamAssassin as an ACL.  **NOTE:**  The value of this parameter is **always** &#x60;1&#x60; * &#x60;1&#x60; -  SpamAssassin is an ACL. | [optional] 
**spam_auto_delete** | **int** | Whether the user&#39;s autodelete function is enabled.  * &#x60;1&#x60; -  Enabled. * &#x60;0&#x60; -  Not enabled.  **NOTE::**  This key does **not** appear if the &#x60;cpuser_spam_auto_delete&#x60; key appears | [optional] 
**spam_auto_delete_score** | **int** | Displays the user&#39;s spam filter threshold.  For more information, see &#x60;Email::add_spam_filter&#x60;.  **Note:**  This key does **not** appear if the &#x60;cpuser_spam_auto_delete_score&#x60; key appears | [optional] 
**spam_box_enabled** | **int** | Whether the user&#39;s spam box is enabled.  * &#x60;1&#x60; -  Enabled. * &#x60;0&#x60; -  Not enabled. | [optional] 
**spam_enabled** | **int** | Whether the server&#39;s global spam filtering is enabled.  * &#x60;1&#x60; -  Enabled. * &#x60;0&#x60; -  Not enabled.  **Note:**   This value will **only** return &#x60;0&#x60; if the cPanel user disables Apache SpamAssassin. | [optional] 
**spam_status_changeable** | **int** | Whether the server allows cPanel users to configure Apache SpamAssassin settings.  * &#x60;1&#x60; -  Allowed. * &#x60;0&#x60; -  Not allowed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200175_result_data import InlineResponse200175ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200175ResultData from a JSON string
inline_response200175_result_data_instance = InlineResponse200175ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200175ResultData.to_json())

# convert the object into a dict
inline_response200175_result_data_dict = inline_response200175_result_data_instance.to_dict()
# create an instance of InlineResponse200175ResultData from a dict
inline_response200175_result_data_from_dict = InlineResponse200175ResultData.from_dict(inline_response200175_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



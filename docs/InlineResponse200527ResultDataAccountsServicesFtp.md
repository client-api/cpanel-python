# InlineResponse200527ResultDataAccountsServicesFtp

Information about the Subaccount's FTP status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the Subaccount can access FTP.  * &#x60;1&#x60; — Has FTP service access. * &#x60;0&#x60; — Does **not** have FTP service access. | [optional] 
**homedir** | **str** | The Subaccount&#39;s FTP directory, relative to the cPanel account&#39;s home directory. | [optional] 
**quota** | **int** | The Subaccount&#39;s FTP maximum disk space quota, in megabytes (MB).  * &#x60;0&#x60; — The account has an unlimited disk space quota. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts_services_ftp import InlineResponse200527ResultDataAccountsServicesFtp

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccountsServicesFtp from a JSON string
inline_response200527_result_data_accounts_services_ftp_instance = InlineResponse200527ResultDataAccountsServicesFtp.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccountsServicesFtp.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_services_ftp_dict = inline_response200527_result_data_accounts_services_ftp_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccountsServicesFtp from a dict
inline_response200527_result_data_accounts_services_ftp_from_dict = InlineResponse200527ResultDataAccountsServicesFtp.from_dict(inline_response200527_result_data_accounts_services_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



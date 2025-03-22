# InlineResponse200541ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_enabled** | **int** | Whether the user has backups enabled. * &#x60;1&#x60; - Backups enabled. * &#x60;0&#x60; - Backups not enabled. | [optional] 
**bandwidth_limit** | **int** | The account&#39;s bandwidth limit. * &#x60;0&#x60; - unlimited * A maximum amount of bandwidth, in bytes. | [optional] 
**cgi_enabled** | **int** | Whether CGI is enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**contact_email** | **str** | The account&#39;s contact email address. | [optional] 
**contact_email_2** | **str** | The account&#39;s alternate contact email address, if one exists. | [optional] 
**cpanel_root_directory** | **str** | The &#x60;root&#x60; directory. | [optional] 
**created** | **int** | The account&#39;s creation date in [Unix time](http://en.wikipedia.org/wiki/Unix_time) format. | [optional] 
**created_in_version** | **str** | The version of cPanel used during account creation. | [optional] 
**database_owner** | **str** | The owner of the account&#39;s databases. * &#x60;root&#x60; * A reseller account&#39;s username. * The account&#39;s username. | [optional] 
**dead_domains** | **List[str]** | The account&#39;s inactive domains. | [optional] 
**demo_mode** | **int** | Whether demo mode is enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disk_block_limit** | **int** | The number of disk blocks for the account. * &#x60;0&#x60; - unlimited * A maximum amount of disk blocks, in kilobytes. | [optional] 
**dkim_enabled** | **int** | Whether DomainKeys Identified Mail (DKIM) is enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**domain** | **str** | The account&#39;s main domain. | [optional] 
**domains** | **List[str]** | list of the account&#39;s domains and subdomains. | [optional] 
**feature** | [**InlineResponse200541ResultDataFeature**](InlineResponse200541ResultDataFeature.md) |  | [optional] 
**feature_list** | **str** | The account&#39;s [feature list](https://go.cpanel.net/whmdocs84FeatureManager) name. | [optional] 
**gid** | **int** | The account&#39;s group ID. | [optional] 
**home** | **str** | The user&#39;s home directory. | [optional] 
**home_directory_links** | **List[object]** | Any symlinks to the cPanel account&#39;s home directory. An array of one or more home directory symlinks. | [optional] 
**ip** | **str** | The account&#39;s IPv4 address. | [optional] 
**lang** | **str** | The account&#39;s language. | [optional] 
**last_modified** | **int** | The most recent modification time of the &#x60;/var/cpanel/users/user&#x60; file in [Unix time format](https://en.wikipedia.org/wiki/Unix_time).  **Note:**  &#x60;user&#x60; represents the cPanel user. | [optional] 
**legacy_backup_enabled** | **int** | Whether legacy backups are enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled. | [optional] 
**locale** | **str** | The account&#39;s default locale, a two-letter [ISO-3166 code](http://www.iso.org/iso/country_codes.htm). | [optional] 
**mailbox_format** | **str** | The storage format that the account&#39;s mailboxes use. * &#x60;maildir&#x60; * &#x60;mbox&#x60; | [optional] 
**maximum_addon_domains** | [**InlineResponse200541ResultDataMaximumAddonDomains**](InlineResponse200541ResultDataMaximumAddonDomains.md) |  | [optional] 
**maximum_databases** | [**InlineResponse200541ResultDataMaximumDatabases**](InlineResponse200541ResultDataMaximumDatabases.md) |  | [optional] 
**maximum_defer_fail_percentage** | [**InlineResponse200541ResultDataMaximumDeferFailPercentage**](InlineResponse200541ResultDataMaximumDeferFailPercentage.md) |  | [optional] 
**maximum_email_account_disk_quota** | [**InlineResponse200541ResultDataMaximumEmailAccountDiskQuota**](InlineResponse200541ResultDataMaximumEmailAccountDiskQuota.md) |  | [optional] 
**maximum_emails_per_hour** | [**InlineResponse200541ResultDataMaximumEmailsPerHour**](InlineResponse200541ResultDataMaximumEmailsPerHour.md) |  | [optional] 
**maximum_ftp_accounts** | [**InlineResponse200541ResultDataMaximumFtpAccounts**](InlineResponse200541ResultDataMaximumFtpAccounts.md) |  | [optional] 
**maximum_mail_accounts** | [**InlineResponse200541ResultDataMaximumMailAccounts**](InlineResponse200541ResultDataMaximumMailAccounts.md) |  | [optional] 
**maximum_mailing_lists** | [**InlineResponse200541ResultDataMaximumMailingLists**](InlineResponse200541ResultDataMaximumMailingLists.md) |  | [optional] 
**maximum_parked_domains** | [**InlineResponse200541ResultDataMaximumParkedDomains**](InlineResponse200541ResultDataMaximumParkedDomains.md) |  | [optional] 
**maximum_passenger_apps** | [**InlineResponse200541ResultDataMaximumPassengerApps**](InlineResponse200541ResultDataMaximumPassengerApps.md) |  | [optional] 
**maximum_subdomains** | [**InlineResponse200541ResultDataMaximumSubdomains**](InlineResponse200541ResultDataMaximumSubdomains.md) |  | [optional] 
**mxcheck** | [**InlineResponse200541ResultDataMxcheck**](InlineResponse200541ResultDataMxcheck.md) |  | [optional] 
**notify_account_authn_link** | **int** | Whether the systems sends a notification when someone links the account to an external authentication account. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_account_authn_link_notification_disabled** | **int** | Whether the systems sends a notification when someone disables notifications for external authentication account links. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_account_login** | **int** | Whether the system sends a notification when someone logs in to the account. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_account_login_for_known_netblock** | **int** | Whether the system sends a notification when a user on a known netblock logs in to the account. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_account_login_notification_disabled** | **int** | Whether the system sends a notification when someone disables notifications for account logins. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_autossl_expiry** | **int** | Whether the system sends a notification when an AutoSSL certificate expires. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify | [optional] 
**notify_autossl_expiry_coverage** | **int** | Whether the system sends a notification when AutoSSL cannot renew a certificate because domains that fail Domain Control Validation (DCV) exist on the current certificate. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_autossl_renewal_coverage** | **int** | Whether the system sends a notification when AutoSSL renews a certificate. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_autossl_renewal_coverage_reduced** | **int** | Whether the system sends a notification when AutoSSL renews a certificate, but the new certificate lacks at least one domain that the previous certificate secured. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_autossl_renewal_uncovered_domains** | **int** | Whether the system sends a notification when AutoSSL renews a certificate, but the new certificate lacks at least one domain that the previous certificate secured. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_bandwidth_limit** | **int** | Whether the systems sends a notification when the account reaches its bandwidth quota. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_contact_address_change** | **int** | Whether the systems sends a notification when someone changes the contact address for the account. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_contact_address_change_notification_disabled** | **int** | Whether the systems sends a notification when someone disables the notification for contact address changes. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_disk_limit** | **int** | Whether the systems sends a notification when the account reaches its disk usage limit. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_password_change** | **int** | Whether the systems sends a notification when someone changes the account&#39;s password. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_password_change_notification_disabled** | **int** | Whether the systems sends a notification when someone disables notifications for password changes. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_ssl_expiry** | **int** | Whether the systems sends a notification when an SSL certificate on the account expires. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_twofactorauth_change** | **int** | Whether the systems sends a notification when the account&#39;s Two-Factor Authentication (2FA) credentials change. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**notify_twofactorauth_change_notification_disabled** | **int** | Whether the systems sends a notification when someone disables notifications for 2FA. * &#x60;1&#x60; - Notifies. * &#x60;0&#x60; - Doesn&#39;t notify. | [optional] 
**owner** | **str** | The account&#39;s owner. * &#x60;root&#x60; * A reseller account&#39;s username. * The account&#39;s username. | [optional] 
**package_extensions** | **List[str]** | The account&#39;s package extensions. | [optional] 
**plan** | **str** | The account&#39;s hosting package. | [optional] 
**pushbullet_access_token** | **str** | The account&#39;s Pushbullet access token. | [optional] 
**shell** | **str** | The account&#39;s shell. | [optional] 
**spf_enabled** | **int** | Whether Sender Policy Framework (SPF) is enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**ssl_default_key_type** | **str** | The type of key to generate for the user’s TLS certificates and CSRs.  * &#x60;system&#x60; — The system’s &#x60;ssl_default_key_type&#x60; value in the [&#x60;cpanel.config&#x60; file](https://go.cpanel.net/ThecpanelconfigFile). * &#x60;rsa-2048&#x60; — 2,048-bit RSA. * &#x60;rsa-4096&#x60; — 4,096-bit RSA. * &#x60;ecdsa-prime256v1&#x60; — ECDSA prime256v1 (“P-256”). * &#x60;ecdsa-secp384r1&#x60; — ECDSA secp384r1 (“P-384”). | [optional] 
**theme** | **str** | The account&#39;s current theme. | [optional] 
**uid** | **int** | The account&#39;s user ID on the system. | [optional] 
**user** | **str** | An existing account&#39;s username. | [optional] 
**utf8_mailbox** | **int** | Whether UTF-8-encoded mailbox names are enabled for the cPanel account. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200541_result_data import InlineResponse200541ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200541ResultData from a JSON string
inline_response200541_result_data_instance = InlineResponse200541ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200541ResultData.to_json())

# convert the object into a dict
inline_response200541_result_data_dict = inline_response200541_result_data_instance.to_dict()
# create an instance of InlineResponse200541ResultData from a dict
inline_response200541_result_data_from_dict = InlineResponse200541ResultData.from_dict(inline_response200541_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



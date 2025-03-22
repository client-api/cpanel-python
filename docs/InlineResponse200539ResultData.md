# InlineResponse200539ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_park_subdomain_on_hostname** | **int** | Whether the system allows users to park subdomains of the server&#39;s hostname.  * &#x60;1&#x60; - Allows. * &#x60;0&#x60; - Doesn&#39;t allow. | [optional] 
**allow_remote_domains** | **int** | Whether the system allows users to create addon domains or aliases that resolve to other servers.  * &#x60;1&#x60; - Allows. * &#x60;0&#x60; - Doesn&#39;t allow. | [optional] 
**allow_reset_password** | **int** | Whether cPanel&#39;s [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for the account.  * &#x60;1&#x60; - *Reset Password* feature enabled. * &#x60;0&#x60; - *Reset Password* feature not enabled. | [optional] 
**allow_reset_password_for_subaccounts** | **int** | Whether cPanel&#39;s [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for subaccounts on the account.  * &#x60;1&#x60; - *Reset Password* feature enabled. * &#x60;0&#x60; - *Reset Password* feature not enabled. | [optional] 
**allow_unregistered_domains** | **int** | Whether the system allows users to add domains they didn&#39;t register with a domain name registrar.  * &#x60;1&#x60; - Allows. * &#x60;0&#x60; - Doesn&#39;t allow. | [optional] 
**apache_port** | **str** | The IP address or IP address with a firewall port number that Apache uses to listen for requests and serve web pages over an unsecured connection. | [optional] 
**apache_ssl_port** | **str** | The IP address or IP address with a firewall port number that Apache uses to listen for requests and serve web pages over a secure connection. | [optional] 
**api_shell** | **int** | Whether the user can access cPanel&#39;s [*API Shell*](https://go.cpanel.net/cpaneldocsAPIShell) interface (*cPanel &gt;&gt; Home &gt;&gt; Advanced &gt;&gt; API Shell*).  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - Can&#39;t access. | [optional] 
**awstats_browser_update** | **int** | Whether the user can update their [AWStats](http://awstats.sourceforge.net/) software.  * &#x60;1&#x60; - Can update. * &#x60;0&#x60; - Can&#39;t update. | [optional] 
**awstats_reverse_dns** | **int** | Whether the AWStats statistical analysis software interprets visitors&#39; domain names as IP addresses.  * &#x60;1&#x60; - Interprets visitors&#39; domain names as IP addresses. * &#x60;0&#x60; - Doesn&#39;t interpret visitors&#39; domain names as IP addresses. | [optional] 
**cpanel_root_directory** | **str** | The cPanel &#x60;root&#x60; directory. | [optional] 
**database_prefix_required** | **int** | Whether the account requires database prefixing.  * &#x60;1&#x60; - Requires database prefixing. * &#x60;0&#x60; - Doesn&#39;t require database prefixing. | [optional] 
**default_theme** | **str** | The cPanel interface&#39;s default theme. | [optional] 
**disable_analog** | **int** | Whether users can access the [*Analog Stats*](https://go.cpanel.net/cpaneldocsAnalogStats) interface (*cPanel &gt;&gt; Home &gt;&gt; Metrics &gt;&gt; Analog Stats*).  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_awstats** | **int** | Whether the [AWStats](http://awstats.sourceforge.net/) software is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_boxtrapper** | **int** | Whether [*BoxTrapper*](https://go.cpanel.net/cpaneldocsBoxTrapper) is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_mailman** | **int** | Whether Mailman mailing lists are enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_roundcube** | **int** | Whether [Roundcube webmail](https://roundcube.net/) is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_spamassassin** | **int** | Whether the Apache SpamAssassin spam filter is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_spambox** | **int** | Whether Apache SpamAssassin&#39;s spam box feature is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**disable_webalizer** | **int** | Whether the [Webalizer](http://www.webalizer.org/) statistics program is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**display_cpanel_doclinks** | **int** | Whether the system displays links to cPanel feature documentation in the cPanel interface.  * &#x60;1&#x60; - Displays documentation links. * &#x60;0&#x60; - Doesn&#39;t display documentation links. | [optional] 
**dnsadmin_app** | **str** | The application that processes DNS management requests.  * The value is an application&#39;s file path, relative to the user&#39;s home directory. * &#x60;dnsadmin&#x60; * &#x60;auto-detect SSL&#x60; | [optional] 
**docroots_in_public_html_only** | **int** | Whether the system restricts users from creating addon domains and subdomains outside of their &#x60;public_html&#x60; directory.  * &#x60;1&#x60; - Restricts users from creating addon domains and subdomains outside of their &#x60;public_html&#x60; directory. * &#x60;0&#x60; - Allows users to creating addon domains and subdomains outside of their &#x60;public_html&#x60; directory. | [optional] 
**email_filter_storage_directory** | **str** | The location of the Exim email filter storage directory. | [optional] 
**empty_trash_days** | **str** | The minimum age of files that the system will automatically purge from &#x60;.trash&#x60; folders in user home directories. | [optional] 
**enable_file_protect** | **int** | Whether [EasyApache 4&#39;s *FileProtect* option](https://go.cpanel.net/EasyApache4FileprotectOption) is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**file_upload_maximum_bytes** | **int** | The maximum file size, in megabytes (MB), that a user can upload to a server. | [optional] 
**file_upload_must_leave_bytes** | **int** | The minimum filesystem quota that the system requires after a file uploads to a server. | [optional] 
**file_usage** | **int** | Whether file usage information displays in the cPanel *Home* interface&#39;s statistics bar.  * &#x60;1&#x60; - Displays file usage information. * &#x60;0&#x60; - Doesn&#39;t display file usage information. | [optional] 
**ftp_server** | **str** | The FTP server.  * &#x60;pure-ftpd&#x60; - The Pure-FTPD server. * &#x60;proftpd&#x60; - The ProFTPD FTP server. * &#x60;disabled&#x60; - FTP has been disabled on this server. | [optional] 
**htaccess_check_recurse** | **int** | The maximum number of directories deep to look for &#x60;.htaccess&#x60; files when you change the PHP handler. | [optional] 
**invite_sub** | **int** | Whether cPanel account users can send invitations to new Subaccount users via cPanel&#39;s [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (*cPanel &gt;&gt; Home &gt;&gt; Preferences &gt;&gt; User Manager*).  * &#x60;1&#x60; - Can send invitations. * &#x60;0&#x60; - Can&#39;t send invitations. | [optional] 
**ipv6_listen** | **int** | Whether the &#x60;cpsrvd&#x60; daemon and other cPanel &amp; WHM services listen on IPv6.  * &#x60;1&#x60; - Listen on IPv6. * &#x60;0&#x60; - Don&#39;t listen on IPv6. | [optional] 
**is_mod_userdir_enabled** | **int** | Whether the [Apache &#x60;mod_userdir&#x60; Tweak](https://go.cpanel.net/whmdocsApachemod_userdirTweak) is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**local_nameserver_type** | **str** | The DNS nameserver&#39;s type.  * &#x60;powerdns&#x60; - The PowerDNS nameserver. * &#x60;bind&#x60; - The bind nameserver. * &#x60;disabled&#x60; - Nameserver&#39;s have been disabled on this server. | [optional] 
**logout_redirect_url** | **str** | The logout redirection URL. | [optional] 
**mail_server** | **str** | The mailserver type.  * &#x60;dovecot&#x60; - The Dovecot mailserver. * &#x60;disabled&#x60; - The mailserver is disabled on this system. | [optional] 
**mailbox_storage_format** | **str** | The mailbox storage format for new accounts.  * &#x60;mdbox&#x60; - The mdbox storage format. * &#x60;maildir&#x60; - The maildir storage format. | [optional] 
**minimum_password_strength** | **int** | The minimum strength for cPanel account passwords. | [optional] 
**minimum_password_strength_mysql** | **int** | The minimum strength for MySQL or MariaDB passwords. | [optional] 
**mysql_host** | **str** | The MySQL or MariaDB hostname or IP address. | [optional] 
**mysql_version** | **str** | The MySQL or MariaDB version. | [optional] 
**php_loader** | **str** | The PHP loaders through which the system executes internal PHP scripts.  * &#x60;ioncube&#x60; - The ionCube PHP loader. * &#x60;sourceguardian&#x60; - The SourceGuardian PHP loader. * &#x60;ioncube,sourceguardian&#x60; - Both the ionCube and SourceGuardian PHP loaders are in use. * An emtpy string - PHP loader is not in use. | [optional] 
**php_maximum_execution_time** | **int** | The number of seconds that a PHP script can run before the system terminates it. | [optional] 
**php_open_basedir_home** | **int** | Whether PHP &#x60;open_basedir&#x60; protection is enabled on the server.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled.  **Important:**  We removed WHM&#39;s *PHP open_basedir Tweak* interface (*WHM &gt;&gt; Home &gt;&gt; Security Center &gt;&gt; PHP open_basedir Tweak*) | [optional] 
**php_post_maximum_size** | **int** | The maximum size, in megabytes (MB), of a POST request. | [optional] 
**php_system_default_version** | **str** | The system&#39;s default version of PHP. | [optional] 
**php_upload_maximum_filesize** | **int** | The maximum file size, in megabytes (MB), that a PHP script may upload. | [optional] 
**phpmyadmin_disable_search_info_schema** | **int** | Whether the user can search for the phpMyAdmin information schema.  * &#x60;1&#x60; - Searches are enabled. * &#x60;0&#x60; - Searches are **not** enabled. | [optional] 
**require_ssl** | **int** | Whether the system requires passwords and other sensitive information use SSL encryption.  * &#x60;1&#x60; - Requires SSL. * &#x60;0&#x60; - Doesn&#39;t require SSL. | [optional] 
**skip_apache_clients_optimizer** | **int** | Whether the Apache Client Optimizer is enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**skip_bandwidth_limit_check** | **int** | Whether the system automatically suspends HTTP service for accounts that exceed their bandwidth limit.  * &#x60;1&#x60; - Suspends HTTP service. * &#x60;0&#x60; - Doesn&#39;t suspend HTTP service. | [optional] 
**skip_mailbox_warnings_check** | **int** | Whether mailbox usage warnings are enabled.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**ssl_default_key_type** | **str** | The default SSL/TLS encryption algorithm used by the system.  * &#x60;rsa-2048&#x60; - The rsa-2048 encryption algorithm. * &#x60;ecdsa-secp384r1&#x60; - The ecdsa-secp384r1 encryption algorithm. * &#x60;ecdsa-prime256v1&#x60; - The ecdsa-prime256v1 encryption algorithm. * &#x60;rsa-4096&#x60; - The rsa-4096 encryption algorithm. | [optional] 
**use_information_schema** | **int** | Whether the system uses the MySQL &#x60;INFORMATION_SCHEMA&#x60; view. This view includes disk usage by all MySQL tables in the disk usage totals.  * &#x60;1&#x60; - Uses MySQL&#39;s &#x60;INFORMATION_SCHEMA&#x60; view. * &#x60;0&#x60; - Doesn&#39;t use MySQL&#39;s &#x60;INFORMATION_SCHEMA&#x60; view. | [optional] 
**use_mail_for_mailman_url** | **int** | Whether the system prefixes Mailman URLs with mail. For example, &#x60;http://mail.domain.com/mailman&#x60;.  * &#x60;1&#x60; - Prefixes Mailman URLs with the &#x60;mail.&#x60; prefix. * &#x60;0&#x60; - Doesn&#39;t prefix Mailman URLs with the &#x60;mail.&#x60; prefix. | [optional] 
**version** | **str** | The system&#39;s Linux Kernel version. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200539_result_data import InlineResponse200539ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200539ResultData from a JSON string
inline_response200539_result_data_instance = InlineResponse200539ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200539ResultData.to_json())

# convert the object into a dict
inline_response200539_result_data_dict = inline_response200539_result_data_instance.to_dict()
# create an instance of InlineResponse200539ResultData from a dict
inline_response200539_result_data_from_dict = InlineResponse200539ResultData.from_dict(inline_response200539_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



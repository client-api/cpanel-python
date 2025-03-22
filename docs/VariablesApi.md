# clientapi_cpanel.VariablesApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session_information**](VariablesApi.md#get_session_information) | **GET** /Variables/get_session_information | Return web server&#39;s hostname
[**variables_get_server_information**](VariablesApi.md#variables_get_server_information) | **GET** /Variables/get_server_information | Return server&#39;s configuration settings
[**variables_get_user_information**](VariablesApi.md#variables_get_user_information) | **GET** /Variables/get_user_information | Return cPanel account&#39;s configuration settings


# **get_session_information**
> InlineResponse200540 get_session_information(name=name)

Return web server's hostname

This function retrieves a web server's hostname.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200540 import InlineResponse200540
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.VariablesApi(api_client)
    name = host # str | The web server environment variable to retrieve. You can **only** retrieve the web server's hostname.  * `host` is the only possible value. (optional) (default to host)

    try:
        # Return web server's hostname
        api_response = api_instance.get_session_information(name=name)
        print("The response of VariablesApi->get_session_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->get_session_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The web server environment variable to retrieve. You can **only** retrieve the web server&#39;s hostname.  * &#x60;host&#x60; is the only possible value. | [optional] [default to host]

### Return type

[**InlineResponse200540**](InlineResponse200540.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_get_server_information**
> InlineResponse200539 variables_get_server_information(name=name)

Return server's configuration settings

This function retrieves the configuration settings for the cPanel & WHM server on which an account exists. This is useful, for example, to verify which applications and functionality are available on the account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200539 import InlineResponse200539
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.VariablesApi(api_client)
    name = 'name=allow_park_subdomain_on_hostname&name=allow_remote_domains&name=allow_reset_password' # str | The server configuration settings to return.  <details> <summary>Click to view information about the available server configuration settings.</summary>  * `default_theme` - The cPanel interface's default theme. * `email_filter_storage_directory` - The location of the Exim email filter storage directory. * `allow_park_subdomain_on_hostname` - Whether the system allows users to park subdomains of the server's hostname. * `allow_remote_domains` - Whether the system allows users to create addon domains or aliases that resolve to other servers. * `allow_unregistered_domains` - Whether the system allows users to add domains they didn't register with a domain name registrar. * `apache_port` - The IP address or IP address with a firewall port number that Apache® uses to listen for requests and serve web pages over an unsecured connection. * `apache_ssl_port` - The port or IP address that Apache uses to listen for requests and serve web pages over a secure connection. * `api_shell` - Whether the user can access cPanel's [*API Shell*](https://go.cpanel.net/cpaneldocsAPIShell) interface (*cPanel >> Home >> Advanced >> API Shell*). * `awstats_browser_update` - Whether the user can update their [AWStats](http://awstats.sourceforge.net/) software. * `awstats_reverse_dns` - Whether the AWStats statistical analysis software interprets visitors' domain names as IP addresses. * `cpanel_root_directory` - The cPanel `root` directory. * `database_prefix_required` - Whether the account requires database prefixing. * `display_cpanel_doclinks` - Whether the system displays links to cPanel feature documentation in the cPanel interface. * `dnsadmin_app` - The application that processes DNS management requests. * `empty_trash_days` - The minimum age of files that the system will automatically purge from `.trash` folders in user home directories. * `enable_file_protect` - Whether [EasyApache 4's *FileProtect* option](https://go.cpanel.net/EasyApache4FileprotectOption) is enabled. * `file_upload_maximum_bytes` - The maximum file size, in megabytes (MB), that a user can upload to a server. * `file_upload_must_leave_bytes` - The minimum filesystem quota that the system requires after a file uploads to a server. * `file_usage` - Whether file usage information displays in the cPanel *Home* interface's statistics bar. * `ftp_server` - The FTP server. * `htaccess_check_recurse` - The maximum number of directories deep to look for `.htaccess` files when you change the PHP handler. * `invite_sub` - Whether cPanel account users can send invitations to new Subaccount users via cPanel's [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (*cPanel >> Home >> Preferences >> User Manager*). * `ipv6_listen` - Whether the `cpsrvd` daemon and other cPanel & WHM services listen on IPv6. * `local_nameserver_type` - The DNS nameserver's type. * `logout_redirect_url` - The logout redirection URL. * `mailbox_storage_format` - The mailbox storage format for new accounts. * `mail_server` - The mailserver type. * `minimum_password_strength` - The minimum strength for cPanel account passwords.  * `minimum_password_strength_mysql` - The minimum strength for MySQL® or MariaDB® passwords. * `mysql_host` - The MySQL or MariaDB hostname or IP address. * `mysql_version` - The MySQL or MariaDB version. * `php_maximum_execution_time` - The number of seconds that a PHP script can run before the system terminates it. * `php_post_maximum_size` - The maximum size, in megabytes (MB), of a POST request. * `php_system_default_version` - The system's default version of PHP. * `php_upload_maximum_filesize` - The maximum file size, in megabytes (MB), that a PHP script may upload. * `php_loader` - The PHP loaders through which the system executes internal PHP scripts. * `php_open_basedir_home` - Whether PHP `open_basedir` protection is enabled on the server. * `phpmyadmin_disable_search_info_schema` - Whether the user can search for the phpMyAdmin information schema. * `docroots_in_public_html_only` - Whether the system restricts users from creating addon domains and subdomains outside of their `public_html` directory. * `require_ssl` - Whether the system requires passwords and other sensitive information use SSL encryption. * `allow_reset_password` - Whether cPanel's [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for the account. * `allow_reset_password_for_subaccounts` - Whether cPanel's [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for subaccounts on the account. * `disable_analog` - Whether users can access the [*Analog Stats*](https://go.cpanel.net/cpaneldocsAnalogStats) interface (*cPanel >> Home >> Metrics >> Analog Stats*). * `skip_apache_clients_optimizer` - Whether the Apache Client Optimizer is enabled. * `disable_awstats` - Whether the [AWStats](http://awstats.sourceforge.net/) software is enabled. * `skip_mailbox_warnings_check` - Whether mailbox usage warnings are enabled. * `disable_boxtrapper` - Whether [*BoxTrapper*](https://go.cpanel.net/cpaneldocsBoxTrapper) is enabled. * `skip_bandwidth_limit_check` - Whether the system automatically suspends HTTP service for accounts that exceed their bandwidth limit. * `disable_mailman` - Whether Mailman mailing lists are enabled. * `disable_roundcube` - Whether [Roundcube webmail](https://roundcube.net/) is enabled. * `disable_spamassassin` - Whether the Apache SpamAssassin™ spam filter is enabled. * `disable_spambox` - Whether Apache SpamAssassin's spam box feature is enabled. * `disable_webalizer` - Whether the [Webalizer](https://docs.cpanel.net/cpanel/metrics/webalizer/) statistics program is enabled. * `ssl_default_key_type` - The default SSL/TLS encryption algorithm used by the system. * `use_information_schema` - Whether the system uses the MySQL® `INFORMATION_SCHEMA` view. This view includes disk usage by all MySQL tables in the disk usage totals. * `use_mail_for_mailman_url` - Whether the system prefixes Mailman URLs with the `mail` prefix. For example, `http://mail.domain.com/mailman`. * `is_mod_userdir_enabled` - Whether the [Apache `mod_userdir` Tweak](https://go.cpanel.net/whmdocsApachemod_userdirTweak) is enabled. * `version` - The system's Linux® kernel version. </details>  **Note:**  * If you don't use this parameter, this function returns **all** of the server's configuration settings. * To retrieve multiple variables, increment this parameter. For example, `name-1=variable`, `name-2=variable`, `name-3=variable`. (optional)

    try:
        # Return server's configuration settings
        api_response = api_instance.variables_get_server_information(name=name)
        print("The response of VariablesApi->variables_get_server_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->variables_get_server_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The server configuration settings to return.  &lt;details&gt; &lt;summary&gt;Click to view information about the available server configuration settings.&lt;/summary&gt;  * &#x60;default_theme&#x60; - The cPanel interface&#39;s default theme. * &#x60;email_filter_storage_directory&#x60; - The location of the Exim email filter storage directory. * &#x60;allow_park_subdomain_on_hostname&#x60; - Whether the system allows users to park subdomains of the server&#39;s hostname. * &#x60;allow_remote_domains&#x60; - Whether the system allows users to create addon domains or aliases that resolve to other servers. * &#x60;allow_unregistered_domains&#x60; - Whether the system allows users to add domains they didn&#39;t register with a domain name registrar. * &#x60;apache_port&#x60; - The IP address or IP address with a firewall port number that Apache® uses to listen for requests and serve web pages over an unsecured connection. * &#x60;apache_ssl_port&#x60; - The port or IP address that Apache uses to listen for requests and serve web pages over a secure connection. * &#x60;api_shell&#x60; - Whether the user can access cPanel&#39;s [*API Shell*](https://go.cpanel.net/cpaneldocsAPIShell) interface (*cPanel &gt;&gt; Home &gt;&gt; Advanced &gt;&gt; API Shell*). * &#x60;awstats_browser_update&#x60; - Whether the user can update their [AWStats](http://awstats.sourceforge.net/) software. * &#x60;awstats_reverse_dns&#x60; - Whether the AWStats statistical analysis software interprets visitors&#39; domain names as IP addresses. * &#x60;cpanel_root_directory&#x60; - The cPanel &#x60;root&#x60; directory. * &#x60;database_prefix_required&#x60; - Whether the account requires database prefixing. * &#x60;display_cpanel_doclinks&#x60; - Whether the system displays links to cPanel feature documentation in the cPanel interface. * &#x60;dnsadmin_app&#x60; - The application that processes DNS management requests. * &#x60;empty_trash_days&#x60; - The minimum age of files that the system will automatically purge from &#x60;.trash&#x60; folders in user home directories. * &#x60;enable_file_protect&#x60; - Whether [EasyApache 4&#39;s *FileProtect* option](https://go.cpanel.net/EasyApache4FileprotectOption) is enabled. * &#x60;file_upload_maximum_bytes&#x60; - The maximum file size, in megabytes (MB), that a user can upload to a server. * &#x60;file_upload_must_leave_bytes&#x60; - The minimum filesystem quota that the system requires after a file uploads to a server. * &#x60;file_usage&#x60; - Whether file usage information displays in the cPanel *Home* interface&#39;s statistics bar. * &#x60;ftp_server&#x60; - The FTP server. * &#x60;htaccess_check_recurse&#x60; - The maximum number of directories deep to look for &#x60;.htaccess&#x60; files when you change the PHP handler. * &#x60;invite_sub&#x60; - Whether cPanel account users can send invitations to new Subaccount users via cPanel&#39;s [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (*cPanel &gt;&gt; Home &gt;&gt; Preferences &gt;&gt; User Manager*). * &#x60;ipv6_listen&#x60; - Whether the &#x60;cpsrvd&#x60; daemon and other cPanel &amp; WHM services listen on IPv6. * &#x60;local_nameserver_type&#x60; - The DNS nameserver&#39;s type. * &#x60;logout_redirect_url&#x60; - The logout redirection URL. * &#x60;mailbox_storage_format&#x60; - The mailbox storage format for new accounts. * &#x60;mail_server&#x60; - The mailserver type. * &#x60;minimum_password_strength&#x60; - The minimum strength for cPanel account passwords.  * &#x60;minimum_password_strength_mysql&#x60; - The minimum strength for MySQL® or MariaDB® passwords. * &#x60;mysql_host&#x60; - The MySQL or MariaDB hostname or IP address. * &#x60;mysql_version&#x60; - The MySQL or MariaDB version. * &#x60;php_maximum_execution_time&#x60; - The number of seconds that a PHP script can run before the system terminates it. * &#x60;php_post_maximum_size&#x60; - The maximum size, in megabytes (MB), of a POST request. * &#x60;php_system_default_version&#x60; - The system&#39;s default version of PHP. * &#x60;php_upload_maximum_filesize&#x60; - The maximum file size, in megabytes (MB), that a PHP script may upload. * &#x60;php_loader&#x60; - The PHP loaders through which the system executes internal PHP scripts. * &#x60;php_open_basedir_home&#x60; - Whether PHP &#x60;open_basedir&#x60; protection is enabled on the server. * &#x60;phpmyadmin_disable_search_info_schema&#x60; - Whether the user can search for the phpMyAdmin information schema. * &#x60;docroots_in_public_html_only&#x60; - Whether the system restricts users from creating addon domains and subdomains outside of their &#x60;public_html&#x60; directory. * &#x60;require_ssl&#x60; - Whether the system requires passwords and other sensitive information use SSL encryption. * &#x60;allow_reset_password&#x60; - Whether cPanel&#39;s [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for the account. * &#x60;allow_reset_password_for_subaccounts&#x60; - Whether cPanel&#39;s [*Reset Password*](https://go.cpanel.net/resetsubaccountpass) feature is enabled for subaccounts on the account. * &#x60;disable_analog&#x60; - Whether users can access the [*Analog Stats*](https://go.cpanel.net/cpaneldocsAnalogStats) interface (*cPanel &gt;&gt; Home &gt;&gt; Metrics &gt;&gt; Analog Stats*). * &#x60;skip_apache_clients_optimizer&#x60; - Whether the Apache Client Optimizer is enabled. * &#x60;disable_awstats&#x60; - Whether the [AWStats](http://awstats.sourceforge.net/) software is enabled. * &#x60;skip_mailbox_warnings_check&#x60; - Whether mailbox usage warnings are enabled. * &#x60;disable_boxtrapper&#x60; - Whether [*BoxTrapper*](https://go.cpanel.net/cpaneldocsBoxTrapper) is enabled. * &#x60;skip_bandwidth_limit_check&#x60; - Whether the system automatically suspends HTTP service for accounts that exceed their bandwidth limit. * &#x60;disable_mailman&#x60; - Whether Mailman mailing lists are enabled. * &#x60;disable_roundcube&#x60; - Whether [Roundcube webmail](https://roundcube.net/) is enabled. * &#x60;disable_spamassassin&#x60; - Whether the Apache SpamAssassin™ spam filter is enabled. * &#x60;disable_spambox&#x60; - Whether Apache SpamAssassin&#39;s spam box feature is enabled. * &#x60;disable_webalizer&#x60; - Whether the [Webalizer](https://docs.cpanel.net/cpanel/metrics/webalizer/) statistics program is enabled. * &#x60;ssl_default_key_type&#x60; - The default SSL/TLS encryption algorithm used by the system. * &#x60;use_information_schema&#x60; - Whether the system uses the MySQL® &#x60;INFORMATION_SCHEMA&#x60; view. This view includes disk usage by all MySQL tables in the disk usage totals. * &#x60;use_mail_for_mailman_url&#x60; - Whether the system prefixes Mailman URLs with the &#x60;mail&#x60; prefix. For example, &#x60;http://mail.domain.com/mailman&#x60;. * &#x60;is_mod_userdir_enabled&#x60; - Whether the [Apache &#x60;mod_userdir&#x60; Tweak](https://go.cpanel.net/whmdocsApachemod_userdirTweak) is enabled. * &#x60;version&#x60; - The system&#39;s Linux® kernel version. &lt;/details&gt;  **Note:**  * If you don&#39;t use this parameter, this function returns **all** of the server&#39;s configuration settings. * To retrieve multiple variables, increment this parameter. For example, &#x60;name-1&#x3D;variable&#x60;, &#x60;name-2&#x3D;variable&#x60;, &#x60;name-3&#x3D;variable&#x60;. | [optional] 

### Return type

[**InlineResponse200539**](InlineResponse200539.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_get_user_information**
> InlineResponse200541 variables_get_user_information(name=name)

Return cPanel account's configuration settings

This function retrieves the user's account configuration settings.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200541 import InlineResponse200541
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.VariablesApi(api_client)
    name = 'name-1=mailbox_format&name-2=home&name-3=shell' # str | The user configuration variables to retrieve. If you don't use this parameter, this function returns **all** of the user's configuration data.  **Note:**  To retrieve multiple account configuration settings for a user, increment the parameter name. For example: `name-0`, `name-1`, and `name-2`. (optional)

    try:
        # Return cPanel account's configuration settings
        api_response = api_instance.variables_get_user_information(name=name)
        print("The response of VariablesApi->variables_get_user_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->variables_get_user_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user configuration variables to retrieve. If you don&#39;t use this parameter, this function returns **all** of the user&#39;s configuration data.  **Note:**  To retrieve multiple account configuration settings for a user, increment the parameter name. For example: &#x60;name-0&#x60;, &#x60;name-1&#x60;, and &#x60;name-2&#x60;. | [optional] 

### Return type

[**InlineResponse200541**](InlineResponse200541.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


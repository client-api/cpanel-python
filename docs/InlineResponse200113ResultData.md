# InlineResponse200113ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_aliases_valid** | **int** | Whether a valid SSL certificate exists on the domain&#39;s aliases. * &#x60;1&#x60; - A valid SSL certificate exists on the aliases. * &#x60;0&#x60; - A valid SSL certificate does **not** exist on the aliases.  **Important:**  This return only appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**can_https_redirect** | **int** | Whether a valid SSL certificate exists or AutoSSL runs on the domain. * &#x60;1&#x60; - A valid SSL certificate exists or AutoSSL runs. * &#x60;0&#x60; - A valid SSL certificate does **not** exist, and AutoSSL does not run.  **Important:**  This return only appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**customlog** | [**InlineResponse200113ResultDataCustomlog**](InlineResponse200113ResultDataCustomlog.md) |  | [optional] 
**documentroot** | **str** | The absolute path to the domain&#39;s document root. | [optional] 
**domain** | **str** | The domain name on the cPanel account. | [optional] 
**group** | **str** | The domain&#39;s group name. | [optional] 
**hascgi** | **int** | Whether CGI is enabled for the domain. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled. | [optional] 
**homedir** | **str** | The absolute path to the account&#39;s home directory. | [optional] 
**ifmodulemodsuphpc** | [**InlineResponse200113ResultDataIfmodulemodsuphpc**](InlineResponse200113ResultDataIfmodulemodsuphpc.md) |  | [optional] 
**ip** | **str** | The domain&#39;s IP address. | [optional] 
**is_https_redirecting** | **int** | Whether the domain redirects to https. * &#x60;1&#x60; - Redirects. * &#x60;0&#x60; - Does **not** redirect.  **Important:**  This return only appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**options** | **str** | The Apache &#x60;Options&#x60; directive for the domain. | [optional] 
**owner** | **str** | The WHM account (root or a reseller) that owns the cPanel account. | [optional] 
**phpopenbasedirprotect** | **int** | The domain&#39;s &#x60;open_basedir&#x60; setting. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled.  **Note:**  In EasyApache 4, change this directive in the *Editor Mode* section of WHM&#39;s [*MultiPHP INI Editor*](https://go.cpanel.net/whmdocsMultiPHPINIEditor) interface (*WHM &gt;&gt; Home &gt;&gt; Software &gt;&gt; MultiPHP INI Editor*). | [optional] 
**port** | **int** | Apache&#39;s port to access the domain. | [optional] 
**scriptalias** | [**InlineResponse200113ResultDataScriptalias**](InlineResponse200113ResultDataScriptalias.md) |  | [optional] 
**serveradmin** | **str** | The domain&#39;s administrator&#39;s contact email address. | [optional] 
**serveralias** | **str** | A space-separated list of the domain&#39;s aliases. | [optional] 
**servername** | **str** | The domain&#39;s identifier on the server. | [optional] 
**type** | **str** | The domain type. * &#x60;addon_domain&#x60; - The domain is an addon domain. * &#x60;sub_domain&#x60; - The domain is a subdomain. * &#x60;main_domain&#x60; - The domain is the account&#39;s main domain. * &#x60;parked_domain&#x60; - The domain is a parked domain (domain alias). | [optional] 
**usecanonicalname** | **str** | The domain&#39;s Canonical Name (CNAME) setting. * &#x60;On&#x60; - Use the CNAME. * &#x60;Off&#x60; - Do **not** use the CNAME. | [optional] 
**user** | **str** | The cPanel account&#39;s username. | [optional] 
**userdirprotect** | **int** | The domain&#39;s [Apache &#x60;mod_userdir&#x60; Tweak](https://go.cpanel.net/whmdocsApachemod_userdirTweak) setting. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200113_result_data import InlineResponse200113ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200113ResultData from a JSON string
inline_response200113_result_data_instance = InlineResponse200113ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200113ResultData.to_json())

# convert the object into a dict
inline_response200113_result_data_dict = inline_response200113_result_data_instance.to_dict()
# create an instance of InlineResponse200113ResultData from a dict
inline_response200113_result_data_from_dict = InlineResponse200113ResultData.from_dict(inline_response200113_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



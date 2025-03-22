# MainDomainContents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_aliases_valid** | **int** | Whether a valid SSL certificate exists on the domain&#39;s aliases.  * &#x60;1&#x60; — A valid SSL certificate exists. * &#x60;0&#x60; — A valid SSL certificate does **not** exist.  **Note:**  This return **only** appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**can_https_redirect** | **int** | Whether a valid SSL certificate exists or AutoSSL runs on the domain.  * &#x60;1&#x60; — A valid SSL certificate exists or AutoSSL runs. * &#x60;0&#x60; — A valid SSL certificate does **not** exist and AutoSSL does **not** run.  **Note:**  This return **only** appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**customlog** | [**MainDomainContentsCustomlog**](MainDomainContentsCustomlog.md) |  | [optional] 
**documentroot** | **str** | The absolute path to the domain&#39;s document root. | [optional] 
**domain** | **str** | The domain&#39;s name. | [optional] 
**group** | **str** | The domain&#39;s group. | [optional] 
**hascgi** | **int** | Whether CGI is enabled for the domain.  * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — Disabled. | [optional] 
**homedir** | **str** | The absolute path to the cPanel account&#39;s home directory. | [optional] 
**ifmodulemodsuphpc** | [**MainDomainContentsIfmodulemodsuphpc**](MainDomainContentsIfmodulemodsuphpc.md) |  | [optional] 
**ip** | **str** | The domain&#39;s IPv4 address. | [optional] 
**ipv6** | **str** | The domain&#39;s IPv6 address.  * null — The account does **not** use IPv6. | [optional] 
**is_https_redirecting** | **int** | Whether the domain redirects to &#x60;https&#x60;.  * &#x60;1&#x60; — The domain redirects to &#x60;https&#x60;. * &#x60;0&#x60; — The domain does **not** redirect to &#x60;https&#x60;.  **Note:**  This return **only** appears if you set the &#x60;return_https_redirects_status&#x60; parameter to &#x60;1&#x60;. | [optional] 
**no_cache_update** | **int** | Whether the domain is subject to cache updates.  * &#x60;1&#x60; — The domain updates caches. * &#x60;0&#x60; — The domain does **not** update caches. | [optional] 
**owner** | **str** | The WHM account (&#x60;root&#x60; or a reseller) that owns the cPanel account. | [optional] 
**scriptalias** | [**MainDomainContentsScriptalias**](MainDomainContentsScriptalias.md) |  | [optional] 
**serveradmin** | **str** | The domain&#39;s administrator&#39;s contact email address. | [optional] 
**serveralias** | **str** | A space-separated list of the domain&#39;s aliases. | [optional] 
**servername** | **str** | The domain&#39;s identifier on the server. | [optional] 
**type** | **str** | The domain is the cPanel account&#39;s main domain.  * &#x60;main_domain&#x60; is the only possible value. | [optional] 
**usecanonicalname** | **str** | The domain&#39;s Canonical Name (CNAME) setting.  * &#x60;On&#x60; — Use the domain&#39;s CNAME. * &#x60;Off&#x60; — Do **not** use the domain&#39;s CNAME. | [optional] 
**user** | **str** | The cPanel account&#39;s username. | [optional] 
**userdirprotect** | **int** | The domain&#39;s [Apache &#x60;mod_userdir&#x60; Tweak](https://go.cpanel.net/whmdocsApachemod_userdirTweak) setting.  * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — Disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.main_domain_contents import MainDomainContents

# TODO update the JSON string below
json = "{}"
# create an instance of MainDomainContents from a JSON string
main_domain_contents_instance = MainDomainContents.from_json(json)
# print the JSON string representation of the object
print(MainDomainContents.to_json())

# convert the object into a dict
main_domain_contents_dict = main_domain_contents_instance.to_dict()
# create an instance of MainDomainContents from a dict
main_domain_contents_from_dict = MainDomainContents.from_dict(main_domain_contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



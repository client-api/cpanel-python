# InlineResponse200328ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The redirect&#39;s destination URL. | [optional] 
**displaydomain** | **str** | The domain to redirect.  * &#x60;ALL&#x60; is the only possible value. | [optional] 
**displaysourceurl** | **str** | The path to the file within the domain to test, relative to the home directory. | [optional] 
**docroot** | **str** | The absolute file path to the source domain&#39;s document root. | [optional] 
**domain** | **str** | The domain to redirect. | [optional] 
**kind** | **str** | The kind of redirect.  * &#x60;rewrite&#x60; — The request sent a redirect to another path on the server. * &#x60;redirect&#x60; — The request sent a redirect for the URL. * &#x60;redirectmatch&#x60; — The request sent a redirect based on a regular expression match of the URL. | [optional] 
**matchwww** | **int** | Whether the redirect matches &#x60;www.&#x60; subdomains. * &#x60;1&#x60; — Matches. * &#x60;0&#x60; — Does not match. | [optional] 
**matchwww_text** | **str** | Whether the [*Redirect with or without www.* option](https://go.cpanel.net/Redirects) is active.  * &#x60;checked&#x60; — The *Redirect with or without www.* option is active. | [optional] 
**opts** | **str** | The options that the function passes to Apache as part of the [Rewrite rule](https://httpd.apache.org/docs/2.4/rewrite/flags.html#flag_l). | [optional] 
**source** | **str** | The path to the file within the domain to test, relative to the home directory. | [optional] 
**sourceurl** | **str** | The path to the file within the domain to test, relative to the home directory. | [optional] 
**statuscode** | **str** | The [HTTP Status Code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) of the request | [optional] 
**targeturl** | **str** | The redirect&#39;s destination URL. | [optional] 
**type** | **str** | Whether the redirect is permanent or temporary.  * &#x60;permanent&#x60; — The redirect is permanent. * &#x60;temporary&#x60; — The redirect is temporary. | [optional] 
**urldomain** | **str** | The domain to redirect. | [optional] 
**wildcard** | **int** | Whether the wildcard subdomains match.  * &#x60;1&#x60; — Matches. * &#x60;0&#x60; — Does **not** match. | [optional] 
**wildcard_text** | **str** | Whether the [*Wild Card Redirect*](https://go.cpanel.net/Redirects) option is active.  * &#x60;checked&#x60; — The *Wild Card Redirect* option is active. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200328_result_data import InlineResponse200328ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200328ResultData from a JSON string
inline_response200328_result_data_instance = InlineResponse200328ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200328ResultData.to_json())

# convert the object into a dict
inline_response200328_result_data_dict = inline_response200328_result_data_instance.to_dict()
# create an instance of InlineResponse200328ResultData from a dict
inline_response200328_result_data_from_dict = InlineResponse200328ResultData.from_dict(inline_response200328_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



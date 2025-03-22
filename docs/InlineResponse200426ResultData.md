# InlineResponse200426ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**InlineResponse200426ResultCertificate**](InlineResponse200426ResultCertificate.md) |  | [optional] 
**certificate_text** | **str** | The certificate&#39;s text. | [optional] 
**docroot** | **str** | The document root of the domain that the certificate covers. | [optional] 
**domains** | **List[str]** | The domains that the certificate covers. | [optional] 
**fqdns** | **List[str]** | An array of every valid fully qualified domain name (FQDN) on the virtual host, which includes service subdomains (proxy subdomains). | [optional] 
**ip** | [**InlineResponse200426ResultDataIp**](InlineResponse200426ResultDataIp.md) |  | [optional] 
**is_primary_on_ip** | **int** | Whether the website is primary on the IP address. * &#x60;1&#x60; - Primary. * &#x60;0&#x60; - Not primary. | [optional] 
**mail_sni_status** | **int** | Whether SNI is active on the domain. * &#x60;1&#x60; - Active. * &#x60;0&#x60; - Inactive. | [optional] 
**needs_sni** | **int** | Whether the website requires SNI to function. * &#x60;1&#x60; - Requires SNI. * &#x60;0&#x60; - Does not require SNI. | [optional] 
**servername** | **str** | The server&#39;s hostname. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200426_result_data import InlineResponse200426ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200426ResultData from a JSON string
inline_response200426_result_data_instance = InlineResponse200426ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200426ResultData.to_json())

# convert the object into a dict
inline_response200426_result_data_dict = inline_response200426_result_data_instance.to_dict()
# create an instance of InlineResponse200426ResultData from a dict
inline_response200426_result_data_from_dict = InlineResponse200426ResultData.from_dict(inline_response200426_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



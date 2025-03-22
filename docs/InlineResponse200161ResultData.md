# InlineResponse200161ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account&#39;s email address. | [optional] 
**activesync_available** | **int** | Whether the account supports ActiveSync. * &#x60;1&#x60; — Supported. * &#x60;0&#x60; — **Not** supported. | [optional] 
**activesync_host** | **str** | The account&#39;s ActiveSync hostname.  This return **only** appears if &#x60;activesync_available&#x60; is &#x60;1&#x60;. | [optional] 
**activesync_port** | **int** | The account&#39;s ActiveSync SSL/TLS port.  This return **only** appears if &#x60;activesync_available&#x60; is &#x60;1&#x60;. | [optional] 
**activesync_username** | **str** | The account&#39;s ActiveSync username.  This return **only** appears if &#x60;activesync_available&#x60; is &#x60;1&#x60;. | [optional] 
**display** | **str** | The account&#39;s display name. | [optional] 
**domain** | **str** | The account&#39;s domain name. | [optional] 
**from_archiving** | **int** | Whether the account is a mail archive. * &#x60;1&#x60; — The account is a mail archive. * &#x60;0&#x60; — The account is **not** a mail archive. | [optional] 
**has_plaintext_authentication** | **int** | Whether the account supports plaintext authentication.  * &#x60;1&#x60; — Supported. * &#x60;0&#x60; — **Not** supported. | [optional] 
**inbox_host** | **str** | The account&#39;s hostname. | [optional] 
**inbox_insecure_port** | **int** | The account&#39;s insecure inbound port. | [optional] 
**inbox_port** | **int** | The account&#39;s secure inbound port. | [optional] 
**inbox_service** | **str** | The service type that the account uses. * &#x60;imap&#x60; * &#x60;pop&#x60; | [optional] 
**inbox_username** | **str** | The account&#39;s username. | [optional] 
**mail_domain** | **str** | The account&#39;s mail hostname. | [optional] 
**smtp_host** | **str** | The account&#39;s outbound SMTP hostname. | [optional] 
**smtp_insecure_port** | **int** | The account&#39;s insecure outbound SMTP port. | [optional] 
**smtp_port** | **int** | The account&#39;s secure outbound SMTP port. | [optional] 
**smtp_username** | **str** | The account&#39;s SMTP username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200161_result_data import InlineResponse200161ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200161ResultData from a JSON string
inline_response200161_result_data_instance = InlineResponse200161ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200161ResultData.to_json())

# convert the object into a dict
inline_response200161_result_data_dict = inline_response200161_result_data_instance.to_dict()
# create an instance of InlineResponse200161ResultData from a dict
inline_response200161_result_data_from_dict = InlineResponse200161ResultData.from_dict(inline_response200161_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



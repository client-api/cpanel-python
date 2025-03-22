# InlineResponse20074ResultDataSsl

A list of SSL connection configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | [**List[InlineResponse20074ResultDataSslCalendars]**](InlineResponse20074ResultDataSslCalendars.md) | An array of objects containing the user&#39;s calendars. | [optional] 
**contacts** | [**List[InlineResponse20074ResultDataSslContacts]**](InlineResponse20074ResultDataSslContacts.md) | An array of objects containing the user&#39;s address books. | [optional] 
**free_busy** | **str** | The absolute URL path and HTTPS port to the user&#39;s CalDAV &#x60;free-busy-query&#x60; connection.  **Note:**  This information is useful for clients that support Autodiscovery. | [optional] 
**full_server** | **str** | The absolute URL path and HTTPS port to the user&#39;s CalDAV and CardDAV connection information.  **Note:**  This information is useful for clients that do **not** support Autodiscovery. | [optional] 
**is_self_signed** | **int** | Whether the server uses a self-signed certificate.  * &#x60;1&#x60; — Self-signed. * &#x60;0&#x60; — **Not** self-signed. | [optional] 
**port** | **int** | The port number that the system uses for SSL connections. | [optional] 
**server** | **str** | The short server connection string that includes a domain name and a port that uses the HTTPS protocol.  **Note:**  This value is useful for clients that support Autodiscovery. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data_ssl import InlineResponse20074ResultDataSsl

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultDataSsl from a JSON string
inline_response20074_result_data_ssl_instance = InlineResponse20074ResultDataSsl.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultDataSsl.to_json())

# convert the object into a dict
inline_response20074_result_data_ssl_dict = inline_response20074_result_data_ssl_instance.to_dict()
# create an instance of InlineResponse20074ResultDataSsl from a dict
inline_response20074_result_data_ssl_from_dict = InlineResponse20074ResultDataSsl.from_dict(inline_response20074_result_data_ssl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



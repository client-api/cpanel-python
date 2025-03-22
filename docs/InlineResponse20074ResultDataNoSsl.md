# InlineResponse20074ResultDataNoSsl

A list of non-SSL connection configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | [**List[InlineResponse20074ResultDataNoSslCalendars]**](InlineResponse20074ResultDataNoSslCalendars.md) | An array of objects containing the user&#39;s calendars. | [optional] 
**contacts** | [**List[InlineResponse20074ResultDataNoSslContacts]**](InlineResponse20074ResultDataNoSslContacts.md) | An array of objects containing the user&#39;s address books. | [optional] 
**free_busy** | **str** | The absolute URL path and HTTP port to the user&#39;s CalDAV &#x60;free-busy-query&#x60; connection.  **Note:**  This information is useful for clients that support Autodiscovery. | [optional] 
**full_server** | **str** | The absolute URL path and HTTP port to the user&#39;s CalDAV and CardDAV connection information.  **Note:**  This information is useful for clients that do **not** support Autodiscovery. | [optional] 
**port** | **int** | The port number that the system uses for non-SSL connections. | [optional] 
**server** | **str** | The short server connection string that includes a domain name and a port that uses the HTTP protocol. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data_no_ssl import InlineResponse20074ResultDataNoSsl

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultDataNoSsl from a JSON string
inline_response20074_result_data_no_ssl_instance = InlineResponse20074ResultDataNoSsl.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultDataNoSsl.to_json())

# convert the object into a dict
inline_response20074_result_data_no_ssl_dict = inline_response20074_result_data_no_ssl_instance.to_dict()
# create an instance of InlineResponse20074ResultDataNoSsl from a dict
inline_response20074_result_data_no_ssl_from_dict = InlineResponse20074ResultDataNoSsl.from_dict(inline_response20074_result_data_no_ssl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



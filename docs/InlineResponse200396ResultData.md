# InlineResponse200396ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The resource&#39;s UI display name. | [optional] 
**error** | **str** | An error message, if applicable. | [optional] 
**formatter** | [**InlineResponse200396ResultDataFormatter**](InlineResponse200396ResultDataFormatter.md) |  | [optional] 
**id** | **str** | The resource&#39;s reference name. * &#x60;disk_usage&#x60; * &#x60;filesusage&#x60; - This function **only** returns this value if the *Display File Usage information in the cPanel stats bar* setting is enabled in the *Display* section of WHM&#39;s [*Tweak Settings*](https://go.cpanel.net/whmdocsTweakSettings#display) interface (*WHM &gt;&gt; Home &gt;&gt; Server Configuration &gt;&gt; Tweak Settings*). * &#x60;cachedmysqldiskusage&#x60; * &#x60;cachedpostgresdiskusage&#x60; - This function **only** returns this value if [PostgreSQL® databases](https://go.cpanel.net/cpaneldocsPostgreSQLDatabases) are enabled. * &#x60;bandwidth&#x60; * &#x60;addon_domains&#x60; * &#x60;subdomains&#x60; * &#x60;aliases&#x60; * &#x60;email_accounts&#x60; * &#x60;mailing_lists&#x60; - This function **only** returns this value if the Mailman service is enabled in WHM&#39;s [*Service Manager*](https://go.cpanel.net/whmdocsServiceManager) interface (*WHM &gt;&gt; Home &gt;&gt; Service Configuration &gt;&gt; Service Manager*). * &#x60;autoresponders&#x60; * &#x60;forwarders&#x60; * &#x60;email_filters&#x60; * &#x60;ftp_accounts&#x60; - This function **only** returns this value if FTP accounts exist on the server. * &#x60;mysql_databases&#x60; - This function **only** returns this value if MySQL® databases are enabled. * &#x60;postgresql_databases&#x60;  **Note:**  Certain &#x60;id&#x60; values may **not** appear, based on the [server&#39;s current profile](https://go.cpanel.net/howtouseserverprofiles#profiles). | [optional] 
**maximum** | **int** | The resources&#39;s maximum usage value.  **Note:**   This function returns an null value for an (unlimited) quota. | [optional] 
**url** | **str** | The resource&#39;s defined URL link to its corresponding interface, in applicable. | [optional] 
**usage** | **int** | The resource&#39;s current usage value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200396_result_data import InlineResponse200396ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200396ResultData from a JSON string
inline_response200396_result_data_instance = InlineResponse200396ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200396ResultData.to_json())

# convert the object into a dict
inline_response200396_result_data_dict = inline_response200396_result_data_instance.to_dict()
# create an instance of InlineResponse200396ResultData from a dict
inline_response200396_result_data_from_dict = InlineResponse200396ResultData.from_dict(inline_response200396_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



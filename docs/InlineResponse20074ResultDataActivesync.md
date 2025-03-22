# InlineResponse20074ResultDataActivesync

Configuration details for ActiveSync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the server has ActiveSync enabled. * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — **Not** enabled. | [optional] 
**port** | **int** | The port number the system uses for secure ActiveSync connections. | [optional] 
**server** | **str** | The fully qualified domain name to connect to. | [optional] 
**user** | **str** | The cPanel user or email account user to whom the returned connection information pertains.  If you do **not** specify the &#x60;user&#x60; parameter, this function returns the authenticated cPanel user. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data_activesync import InlineResponse20074ResultDataActivesync

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultDataActivesync from a JSON string
inline_response20074_result_data_activesync_instance = InlineResponse20074ResultDataActivesync.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultDataActivesync.to_json())

# convert the object into a dict
inline_response20074_result_data_activesync_dict = inline_response20074_result_data_activesync_instance.to_dict()
# create an instance of InlineResponse20074ResultDataActivesync from a dict
inline_response20074_result_data_activesync_from_dict = InlineResponse20074ResultDataActivesync.from_dict(inline_response20074_result_data_activesync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



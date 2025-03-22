# InlineResponse20074ResultDataNoSslCalendars


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the calendar. | [optional] 
**name** | **str** | The name of the calendar. | [optional] 
**path** | **str** | The relative URL path to the calendar. | [optional] 
**url** | **str** | The absolute URL to the calendar. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data_no_ssl_calendars import InlineResponse20074ResultDataNoSslCalendars

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultDataNoSslCalendars from a JSON string
inline_response20074_result_data_no_ssl_calendars_instance = InlineResponse20074ResultDataNoSslCalendars.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultDataNoSslCalendars.to_json())

# convert the object into a dict
inline_response20074_result_data_no_ssl_calendars_dict = inline_response20074_result_data_no_ssl_calendars_instance.to_dict()
# create an instance of InlineResponse20074ResultDataNoSslCalendars from a dict
inline_response20074_result_data_no_ssl_calendars_from_dict = InlineResponse20074ResultDataNoSslCalendars.from_dict(inline_response20074_result_data_no_ssl_calendars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



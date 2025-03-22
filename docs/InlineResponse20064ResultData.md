# InlineResponse20064ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **str** | Path to the disinfection log file. The log file will contain a list of JSON objects one per line.  If the last line is:  &#x60;{ \&quot;status\&quot;: \&quot;done\&quot; }&#x60;  the requested files with viruses have be handled as requested.  Use the /ClamScanner/check_disinfection_status API to check the status of a running or finished disinfection. | [optional] 
**task_id** | **str** | The Task Queue system&#39;s task ID number. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20064_result_data import InlineResponse20064ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20064ResultData from a JSON string
inline_response20064_result_data_instance = InlineResponse20064ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20064ResultData.to_json())

# convert the object into a dict
inline_response20064_result_data_dict = inline_response20064_result_data_instance.to_dict()
# create an instance of InlineResponse20064ResultData from a dict
inline_response20064_result_data_from_dict = InlineResponse20064ResultData.from_dict(inline_response20064_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



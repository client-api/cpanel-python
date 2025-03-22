# InlineResponse200113ResultDataCustomlog

An object containing Apache log information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The &#x60;target&#x60; log file&#39;s domain. An [Apache log](http://httpd.apache.org/docs/2.2/mod/mod_log_config.html) domain. Generally, this value is &#x60;combined&#x60;. | [optional] 
**target** | **str** | The absolute path to the domain&#39;s log file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200113_result_data_customlog import InlineResponse200113ResultDataCustomlog

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200113ResultDataCustomlog from a JSON string
inline_response200113_result_data_customlog_instance = InlineResponse200113ResultDataCustomlog.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200113ResultDataCustomlog.to_json())

# convert the object into a dict
inline_response200113_result_data_customlog_dict = inline_response200113_result_data_customlog_instance.to_dict()
# create an instance of InlineResponse200113ResultDataCustomlog from a dict
inline_response200113_result_data_customlog_from_dict = InlineResponse200113ResultDataCustomlog.from_dict(inline_response200113_result_data_customlog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



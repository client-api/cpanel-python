# InlineResponse20085ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_serial** | **int** | The DNS zone’s SOA record’s new serial number. You can use this to submit later edits if you track the number of lines each record takes up. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20085_result_data import InlineResponse20085ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20085ResultData from a JSON string
inline_response20085_result_data_instance = InlineResponse20085ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20085ResultData.to_json())

# convert the object into a dict
inline_response20085_result_data_dict = inline_response20085_result_data_instance.to_dict()
# create an instance of InlineResponse20085ResultData from a dict
inline_response20085_result_data_from_dict = InlineResponse20085ResultData.from_dict(inline_response20085_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



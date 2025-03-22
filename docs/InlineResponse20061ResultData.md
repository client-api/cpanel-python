# InlineResponse20061ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | **List[int]** | An array of port numbers on which Exim listens for SSL/TLS connections. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20061_result_data import InlineResponse20061ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20061ResultData from a JSON string
inline_response20061_result_data_instance = InlineResponse20061ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20061ResultData.to_json())

# convert the object into a dict
inline_response20061_result_data_dict = inline_response20061_result_data_instance.to_dict()
# create an instance of InlineResponse20061ResultData from a dict
inline_response20061_result_data_from_dict = InlineResponse20061ResultData.from_dict(inline_response20061_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200275ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[InlineResponse200275ResultDataHost]**](InlineResponse200275ResultDataHost.md) | An array of objects containing information for the host. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200275_result_data import InlineResponse200275ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200275ResultData from a JSON string
inline_response200275_result_data_instance = InlineResponse200275ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200275ResultData.to_json())

# convert the object into a dict
inline_response200275_result_data_dict = inline_response200275_result_data_instance.to_dict()
# create an instance of InlineResponse200275ResultData from a dict
inline_response200275_result_data_from_dict = InlineResponse200275ResultData.from_dict(inline_response200275_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



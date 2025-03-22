# InlineResponse200445ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The CSR&#39;s text. | [optional] 
**details** | [**InlineResponse200445ResultDataDetails**](InlineResponse200445ResultDataDetails.md) |  | [optional] 
**text** | **str** | The parsed information from the OpenSSL command-line tool. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200445_result_data import InlineResponse200445ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200445ResultData from a JSON string
inline_response200445_result_data_instance = InlineResponse200445ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200445ResultData.to_json())

# convert the object into a dict
inline_response200445_result_data_dict = inline_response200445_result_data_instance.to_dict()
# create an instance of InlineResponse200445ResultData from a dict
inline_response200445_result_data_from_dict = InlineResponse200445ResultData.from_dict(inline_response200445_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



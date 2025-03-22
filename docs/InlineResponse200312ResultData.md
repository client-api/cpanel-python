# InlineResponse200312ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**InlineResponse200312ResultDataCertificates**](InlineResponse200312ResultDataCertificates.md) |  | [optional] 
**checkout_url** | **str** | The URL that the cPanel Market provider uses to process payment. | [optional] 
**order_id** | **int** | The order ID that the cPanel Market provider assigned. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200312_result_data import InlineResponse200312ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200312ResultData from a JSON string
inline_response200312_result_data_instance = InlineResponse200312ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200312ResultData.to_json())

# convert the object into a dict
inline_response200312_result_data_dict = inline_response200312_result_data_instance.to_dict()
# create an instance of InlineResponse200312ResultData from a dict
inline_response200312_result_data_from_dict = InlineResponse200312ResultData.from_dict(inline_response200312_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



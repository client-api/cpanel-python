# InlineResponse200303ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_url** | **str** | The location of the provider’s check out page. | [optional] 
**order_id** | **str** | The order’s ID. | [optional] 
**order_items** | **List[object]** | An array of objects that contain information about Items in the shopping cart. The function returns these values in the order in which you called them. This array of objects returns values that vary between providers. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200303_result_data import InlineResponse200303ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200303ResultData from a JSON string
inline_response200303_result_data_instance = InlineResponse200303ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200303ResultData.to_json())

# convert the object into a dict
inline_response200303_result_data_dict = inline_response200303_result_data_instance.to_dict()
# create an instance of InlineResponse200303ResultData from a dict
inline_response200303_result_data_from_dict = InlineResponse200303ResultData.from_dict(inline_response200303_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



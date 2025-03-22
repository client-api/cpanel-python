# InlineResponse200313ResultData

The function only returns these values if the user or users do **not** have the `order_item_id` item in the cPanel Market pending queue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** | The type of error that the function encountered.  * &#x60;EntryDoesNotExist&#x60; — The returned &#x60;order_item_ids&#x60; do not exist in the cPanel Market pending queue for the user. | [optional] 
**order_item_ids** | **List[int]** | An array that lists order item IDs which do not exist in the cPanel Market pending queue for the user. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200313_result_data import InlineResponse200313ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200313ResultData from a JSON string
inline_response200313_result_data_instance = InlineResponse200313ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200313ResultData.to_json())

# convert the object into a dict
inline_response200313_result_data_dict = inline_response200313_result_data_instance.to_dict()
# create an instance of InlineResponse200313ResultData from a dict
inline_response200313_result_data_from_dict = InlineResponse200313ResultData.from_dict(inline_response200313_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



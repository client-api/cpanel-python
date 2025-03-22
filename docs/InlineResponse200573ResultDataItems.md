# InlineResponse200573ResultDataItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_running** | **int** | Whether the system is processing a backup restoration.  * &#x60;0&#x60; - No restoration in progress. This is the only possible value. | [optional] 
**sites** | **object** | Information about the site that the system is actively restoring.  **Note:**  * This function returns an empty array when there is **not** an active backup restoration. This is the only possible value. * We have not implemented this return. | [optional] 
**last_outcome** | [**RestoreNotInProgressLastOutcome**](RestoreNotInProgressLastOutcome.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200573_result_data_items import InlineResponse200573ResultDataItems

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200573ResultDataItems from a JSON string
inline_response200573_result_data_items_instance = InlineResponse200573ResultDataItems.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200573ResultDataItems.to_json())

# convert the object into a dict
inline_response200573_result_data_items_dict = inline_response200573_result_data_items_instance.to_dict()
# create an instance of InlineResponse200573ResultDataItems from a dict
inline_response200573_result_data_items_from_dict = InlineResponse200573ResultDataItems.from_dict(inline_response200573_result_data_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20044ResultDataGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** | The group&#39;s description. | [optional] 
**group** | **str** | The group&#39;s ID. | [optional] 
**items** | [**List[InlineResponse20044ResultDataItems]**](InlineResponse20044ResultDataItems.md) | The groups and their application details. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20044_result_data_groups import InlineResponse20044ResultDataGroups

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20044ResultDataGroups from a JSON string
inline_response20044_result_data_groups_instance = InlineResponse20044ResultDataGroups.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20044ResultDataGroups.to_json())

# convert the object into a dict
inline_response20044_result_data_groups_dict = inline_response20044_result_data_groups_instance.to_dict()
# create an instance of InlineResponse20044ResultDataGroups from a dict
inline_response20044_result_data_groups_from_dict = InlineResponse20044ResultDataGroups.from_dict(inline_response20044_result_data_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200109ResultDataState

A object containing the subdirectory's leech protection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_leech_protection** | **int** | The directory&#39;s leech protection status.  * &#x60;1&#x60; — Leech protection is enabled. * &#x60;0&#x60; — Leech protection is disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_state import InlineResponse200109ResultDataState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataState from a JSON string
inline_response200109_result_data_state_instance = InlineResponse200109ResultDataState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataState.to_json())

# convert the object into a dict
inline_response200109_result_data_state_dict = inline_response200109_result_data_state_instance.to_dict()
# create an instance of InlineResponse200109ResultDataState from a dict
inline_response200109_result_data_state_from_dict = InlineResponse200109ResultDataState.from_dict(inline_response200109_result_data_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



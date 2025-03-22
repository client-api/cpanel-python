# InlineResponse200109ResultDataHomeState

A object containing the `home` directory's leech protection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_leech_protection** | **int** | The home directory&#39;s leech protection status.  * &#x60;1&#x60; — Leech protection is enabled. * &#x60;0&#x60; — Leech protection is disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_home_state import InlineResponse200109ResultDataHomeState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataHomeState from a JSON string
inline_response200109_result_data_home_state_instance = InlineResponse200109ResultDataHomeState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataHomeState.to_json())

# convert the object into a dict
inline_response200109_result_data_home_state_dict = inline_response200109_result_data_home_state_instance.to_dict()
# create an instance of InlineResponse200109ResultDataHomeState from a dict
inline_response200109_result_data_home_state_from_dict = InlineResponse200109ResultDataHomeState.from_dict(inline_response200109_result_data_home_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



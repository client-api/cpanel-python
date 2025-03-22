# InlineResponse200107ResultDataCurrentState

The current subdirectory's privacy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_name** | **str** | The authentication resource name. | [optional] 
**auth_type** | **str** | The directory&#39;s authentication type.  * &#x60;Basic&#x60; * &#x60;None&#x60; | [optional] 
**passwd_file** | **str** | The absolute file path to the directory&#39;s password file. | [optional] 
**protected** | **int** | Whether the directory is protected.  * &#x60;1&#x60; — Protected. * &#x60;0&#x60; — **Not** protected. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200107_result_data_current_state import InlineResponse200107ResultDataCurrentState

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200107ResultDataCurrentState from a JSON string
inline_response200107_result_data_current_state_instance = InlineResponse200107ResultDataCurrentState.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200107ResultDataCurrentState.to_json())

# convert the object into a dict
inline_response200107_result_data_current_state_dict = inline_response200107_result_data_current_state_instance.to_dict()
# create an instance of InlineResponse200107ResultDataCurrentState from a dict
inline_response200107_result_data_current_state_from_dict = InlineResponse200107ResultDataCurrentState.from_dict(inline_response200107_result_data_current_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



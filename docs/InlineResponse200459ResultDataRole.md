# InlineResponse200459ResultDataRole

Information about the user that owns the project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user&#39;s role ID number. | [optional] 
**name** | **str** | The user&#39;s role title. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200459_result_data_role import InlineResponse200459ResultDataRole

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200459ResultDataRole from a JSON string
inline_response200459_result_data_role_instance = InlineResponse200459ResultDataRole.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200459ResultDataRole.to_json())

# convert the object into a dict
inline_response200459_result_data_role_dict = inline_response200459_result_data_role_instance.to_dict()
# create an instance of InlineResponse200459ResultDataRole from a dict
inline_response200459_result_data_role_from_dict = InlineResponse200459ResultDataRole.from_dict(inline_response200459_result_data_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



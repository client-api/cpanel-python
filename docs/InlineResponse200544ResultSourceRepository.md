# InlineResponse200544ResultSourceRepository

An object containing information about the source repository.  **Note:**  The function **only** returns this object if you cloned a source repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_name** | **str** | The source repository&#39;s name. | [optional] 
**url** | **str** | The source repository&#39;s clone URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200544_result_source_repository import InlineResponse200544ResultSourceRepository

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200544ResultSourceRepository from a JSON string
inline_response200544_result_source_repository_instance = InlineResponse200544ResultSourceRepository.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200544ResultSourceRepository.to_json())

# convert the object into a dict
inline_response200544_result_source_repository_dict = inline_response200544_result_source_repository_instance.to_dict()
# create an instance of InlineResponse200544ResultSourceRepository from a dict
inline_response200544_result_source_repository_from_dict = InlineResponse200544ResultSourceRepository.from_dict(inline_response200544_result_source_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200207Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The method name called. | [optional] 
**reason** | **str** | The reason the API function failed when the &#x60;metadata.result&#x60; field is &#x60;0&#x60;. This field may display a success message when a function succeeds. | [optional] 
**result** | **int** | * &#x60;1&#x60; - Success. * &#x60;0&#x60; - Failed. Check the &#x60;reason&#x60; field for more details. | [optional] 
**version** | **int** | The version of the API function. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200207_metadata import InlineResponse200207Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200207Metadata from a JSON string
inline_response200207_metadata_instance = InlineResponse200207Metadata.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200207Metadata.to_json())

# convert the object into a dict
inline_response200207_metadata_dict = inline_response200207_metadata_instance.to_dict()
# create an instance of InlineResponse200207Metadata from a dict
inline_response200207_metadata_from_dict = InlineResponse200207Metadata.from_dict(inline_response200207_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



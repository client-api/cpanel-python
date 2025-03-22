# InlineResponse200335ResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modsec** | [**InlineResponse200335ResultMetadataModsec**](InlineResponse200335ResultMetadataModsec.md) |  | [optional] 
**transformed** | **int** | Post-processing may have transformed the data. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200335_result_metadata import InlineResponse200335ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200335ResultMetadata from a JSON string
inline_response200335_result_metadata_instance = InlineResponse200335ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200335ResultMetadata.to_json())

# convert the object into a dict
inline_response200335_result_metadata_dict = inline_response200335_result_metadata_instance.to_dict()
# create an instance of InlineResponse200335ResultMetadata from a dict
inline_response200335_result_metadata_from_dict = InlineResponse200335ResultMetadata.from_dict(inline_response200335_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



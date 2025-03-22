# InlineResponse2006ResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnt** | **int** | The number of backup files. | [optional] 
**transformed** | **int** | Post-processing may have transformed the data. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response2006_result_metadata import InlineResponse2006ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse2006ResultMetadata from a JSON string
inline_response2006_result_metadata_instance = InlineResponse2006ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(InlineResponse2006ResultMetadata.to_json())

# convert the object into a dict
inline_response2006_result_metadata_dict = inline_response2006_result_metadata_instance.to_dict()
# create an instance of InlineResponse2006ResultMetadata from a dict
inline_response2006_result_metadata_from_dict = InlineResponse2006ResultMetadata.from_dict(inline_response2006_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



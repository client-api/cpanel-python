# InlineResponse200493ResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzers** | [**List[InlineResponse200493ResultMetadataAnalyzers]**](InlineResponse200493ResultMetadataAnalyzers.md) | System configruation for each analyzer. | [optional] 
**locked** | **int** | Whether the analyzer can be turned on or off for the domain by the cPanel user.  - &#x60;1&#x60; - the analyzer cannot be managed by the cPanel user. The reseller or &#x60;root&#x60; controls the configuration. - &#x60;0&#x60; - the analyzer can be managed by the cPanel user. | [optional] 
**transformed** | **int** | Post-processing may have transformed the data. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200493_result_metadata import InlineResponse200493ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200493ResultMetadata from a JSON string
inline_response200493_result_metadata_instance = InlineResponse200493ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200493ResultMetadata.to_json())

# convert the object into a dict
inline_response200493_result_metadata_dict = inline_response200493_result_metadata_instance.to_dict()
# create an instance of InlineResponse200493ResultMetadata from a dict
inline_response200493_result_metadata_from_dict = InlineResponse200493ResultMetadata.from_dict(inline_response200493_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



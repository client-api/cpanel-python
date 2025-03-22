# InlineResponse200493ResultMetadataAnalyzers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_for_user** | **int** | Whether the analyzer can be configured by this user.  - &#x60;1&#x60; - the analyzer can be configured by this user. - &#x60;0&#x60; - the analyzer cannot be configured by this user. | [optional] 
**enabled_by_default** | **int** | Whether the analyzer is turned on or off by default for all users.  - &#x60;1&#x60; - the analyzer is enabled for all users on the server. - &#x60;0&#x60; - the analyzer is disabled for all users on the server. | [optional] 
**name** | **str** | Name of the analyzer.  It must be one of the following:  - &#x60;analog&#x60; - Analog weblog analyzer. - &#x60;awstats&#x60; - AWStats weblog analyzer. - &#x60;webalizer&#x60; - The Webalizer weblog analyzer. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200493_result_metadata_analyzers import InlineResponse200493ResultMetadataAnalyzers

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200493ResultMetadataAnalyzers from a JSON string
inline_response200493_result_metadata_analyzers_instance = InlineResponse200493ResultMetadataAnalyzers.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200493ResultMetadataAnalyzers.to_json())

# convert the object into a dict
inline_response200493_result_metadata_analyzers_dict = inline_response200493_result_metadata_analyzers_instance.to_dict()
# create an instance of InlineResponse200493ResultMetadataAnalyzers from a dict
inline_response200493_result_metadata_analyzers_from_dict = InlineResponse200493ResultMetadataAnalyzers.from_dict(inline_response200493_result_metadata_analyzers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



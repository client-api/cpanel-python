# InlineResponse200494ResultAnalyzers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | Whether the analyzer is turned on or off for the whole server.  - &#x60;1&#x60; - the analyzer is enabled on the server. - &#x60;0&#x60; - the analyzer is disabled on the server. | [optional] 
**enabled** | **int** | Whether the analyzer is turned on or off for the domain.  - &#x60;1&#x60; - the analyzer is enabled. - &#x60;0&#x60; - the analyzer is disabled. | [optional] 
**locked** | **int** | Whether the analyzer can be turned on or off for the domain by the cPanel user.  - &#x60;1&#x60; - the analyzer can be managed by the cPanel user. - &#x60;0&#x60; - the analyzer cannot be managed by the cPanel user. The reseller or &#x60;root&#x60; controls the configuration. | [optional] 
**name** | **str** | Name of the analyzer.  It must be one of the following:  - &#x60;analog&#x60; - Analog weblog analyzer. - &#x60;awstats&#x60; - AWStats weblog analyzer. - &#x60;webalizer&#x60; - The Webalizer weblog analyzer. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200494_result_analyzers import InlineResponse200494ResultAnalyzers

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200494ResultAnalyzers from a JSON string
inline_response200494_result_analyzers_instance = InlineResponse200494ResultAnalyzers.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200494ResultAnalyzers.to_json())

# convert the object into a dict
inline_response200494_result_analyzers_dict = inline_response200494_result_analyzers_instance.to_dict()
# create an instance of InlineResponse200494ResultAnalyzers from a dict
inline_response200494_result_analyzers_from_dict = InlineResponse200494ResultAnalyzers.from_dict(inline_response200494_result_analyzers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



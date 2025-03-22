# InlineResponse200493ResultAnalyzers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the analyzer is turned on or off for the domain.  - &#x60;1&#x60; - the analyzer is enabled. - &#x60;0&#x60; - the analyzer is disabled.  **Note:** This is the cumulative effect of the choices the server admin and user make. | [optional] 
**enabled_by_user** | **int** | Whether the analyzer is turned on or off for the domain specifically by this user.  - &#x60;1&#x60; - the analyzer is enabled by the user. - &#x60;0&#x60; - the analyzer is disabled by the user. | [optional] 
**name** | **str** | Name of the analyzer.  It must be one of the following:  - &#x60;analog&#x60; - Analog weblog analyzer. - &#x60;awstats&#x60; - AWStats weblog analyzer. - &#x60;webalizer&#x60; - The Webalizer weblog analyzer. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200493_result_analyzers import InlineResponse200493ResultAnalyzers

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200493ResultAnalyzers from a JSON string
inline_response200493_result_analyzers_instance = InlineResponse200493ResultAnalyzers.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200493ResultAnalyzers.to_json())

# convert the object into a dict
inline_response200493_result_analyzers_dict = inline_response200493_result_analyzers_instance.to_dict()
# create an instance of InlineResponse200493ResultAnalyzers from a dict
inline_response200493_result_analyzers_from_dict = InlineResponse200493ResultAnalyzers.from_dict(inline_response200493_result_analyzers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



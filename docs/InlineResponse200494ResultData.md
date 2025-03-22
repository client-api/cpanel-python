# InlineResponse200494ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzers** | [**List[InlineResponse200494ResultAnalyzers]**](InlineResponse200494ResultAnalyzers.md) | List of log analyzer configuration objects for this domain | [optional] 
**domain** | **str** | The domain. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200494_result_data import InlineResponse200494ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200494ResultData from a JSON string
inline_response200494_result_data_instance = InlineResponse200494ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200494ResultData.to_json())

# convert the object into a dict
inline_response200494_result_data_dict = inline_response200494_result_data_instance.to_dict()
# create an instance of InlineResponse200494ResultData from a dict
inline_response200494_result_data_from_dict = InlineResponse200494ResultData.from_dict(inline_response200494_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



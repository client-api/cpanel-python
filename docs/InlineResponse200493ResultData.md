# InlineResponse200493ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzers** | [**List[InlineResponse200493ResultAnalyzers]**](InlineResponse200493ResultAnalyzers.md) | List of log analyzer configuration objects for this domain. Only analyzers that are enabled for this user on the system are shown. | [optional] 
**domain** | **str** | The domain. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200493_result_data import InlineResponse200493ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200493ResultData from a JSON string
inline_response200493_result_data_instance = InlineResponse200493ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200493ResultData.to_json())

# convert the object into a dict
inline_response200493_result_data_dict = inline_response200493_result_data_instance.to_dict()
# create an instance of InlineResponse200493ResultData from a dict
inline_response200493_result_data_from_dict = InlineResponse200493ResultData.from_dict(inline_response200493_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



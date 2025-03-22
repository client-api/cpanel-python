# InlineResponse200462ResultDataScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_uptime** | [**Score**](Score.md) |  | [optional] 
**basic_performance** | [**Score**](Score.md) |  | [optional] 
**basic_seo** | [**Score**](Score.md) |  | [optional] 
**basic_content** | [**Score**](Score.md) |  | [optional] 
**basic_tech** | [**Score**](Score.md) |  | [optional] 
**basic_security** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200462_result_data_scores import InlineResponse200462ResultDataScores

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200462ResultDataScores from a JSON string
inline_response200462_result_data_scores_instance = InlineResponse200462ResultDataScores.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200462ResultDataScores.to_json())

# convert the object into a dict
inline_response200462_result_data_scores_dict = inline_response200462_result_data_scores_instance.to_dict()
# create an instance of InlineResponse200462ResultDataScores from a dict
inline_response200462_result_data_scores_from_dict = InlineResponse200462ResultDataScores.from_dict(inline_response200462_result_data_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



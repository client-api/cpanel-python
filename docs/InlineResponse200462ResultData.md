# InlineResponse200462ResultData

An object that contains score details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scores** | [**List[InlineResponse200462ResultDataScores1]**](InlineResponse200462ResultDataScores1.md) | An array of objects containing score data and the associated system information. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200462_result_data import InlineResponse200462ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200462ResultData from a JSON string
inline_response200462_result_data_instance = InlineResponse200462ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200462ResultData.to_json())

# convert the object into a dict
inline_response200462_result_data_dict = inline_response200462_result_data_instance.to_dict()
# create an instance of InlineResponse200462ResultData from a dict
inline_response200462_result_data_from_dict = InlineResponse200462ResultData.from_dict(inline_response200462_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



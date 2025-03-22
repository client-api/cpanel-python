# InlineResponse200486ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklist_from** | **List[str]** | The email addresses on the blacklist. | [optional] 
**required_score** | **List[float]** | The score to mark a message as spam. The system considers mail that matches this score to be spam. | [optional] 
**score** | **List[str]** | The symbolic test name and score. | [optional] 
**whitelist_from** | **List[str]** | The email addresses on the whitelist. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200486_result_data import InlineResponse200486ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200486ResultData from a JSON string
inline_response200486_result_data_instance = InlineResponse200486ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200486ResultData.to_json())

# convert the object into a dict
inline_response200486_result_data_dict = inline_response200486_result_data_instance.to_dict()
# create an instance of InlineResponse200486ResultData from a dict
inline_response200486_result_data_from_dict = InlineResponse200486ResultData.from_dict(inline_response200486_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



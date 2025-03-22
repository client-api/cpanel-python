# InlineResponse200409ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_domains** | **Dict[str, str]** | An object containing the domains that failed to disable  mail SNI. | [optional] 
**updated_domains** | **Dict[str, int]** | AN object containing the domains with disabled mail SNI. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200409_result_data import InlineResponse200409ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200409ResultData from a JSON string
inline_response200409_result_data_instance = InlineResponse200409ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200409ResultData.to_json())

# convert the object into a dict
inline_response200409_result_data_dict = inline_response200409_result_data_instance.to_dict()
# create an instance of InlineResponse200409ResultData from a dict
inline_response200409_result_data_from_dict = InlineResponse200409ResultData.from_dict(inline_response200409_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



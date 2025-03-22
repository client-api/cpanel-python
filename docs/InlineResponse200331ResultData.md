# InlineResponse200331ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_domains_provided** | **int** | Indicates caller error on API call. | [optional] 
**invalid_domains** | **List[str]** | List of invalid domains provided by caller. | [optional] 
**invalid_domains_provided** | **int** | Indicates caller error on API call. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200331_result_data import InlineResponse200331ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200331ResultData from a JSON string
inline_response200331_result_data_instance = InlineResponse200331ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200331ResultData.to_json())

# convert the object into a dict
inline_response200331_result_data_dict = inline_response200331_result_data_instance.to_dict()
# create an instance of InlineResponse200331ResultData from a dict
inline_response200331_result_data_from_dict = InlineResponse200331ResultData.from_dict(inline_response200331_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



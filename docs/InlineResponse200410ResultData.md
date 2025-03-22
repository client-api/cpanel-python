# InlineResponse200410ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_domains** | **Dict[str, str]** | An object that contains the domains that did not enable mail SNI. | [optional] 
**updated_domains** | **Dict[str, int]** | An object that contains the domains with disabled mail SNI. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200410_result_data import InlineResponse200410ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200410ResultData from a JSON string
inline_response200410_result_data_instance = InlineResponse200410ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200410ResultData.to_json())

# convert the object into a dict
inline_response200410_result_data_dict = inline_response200410_result_data_instance.to_dict()
# create an instance of InlineResponse200410ResultData from a dict
inline_response200410_result_data_from_dict = InlineResponse200410ResultData.from_dict(inline_response200410_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200420ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_domain** | **str** | A domain that has AutoSSL disabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200420_result_data import InlineResponse200420ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200420ResultData from a JSON string
inline_response200420_result_data_instance = InlineResponse200420ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200420ResultData.to_json())

# convert the object into a dict
inline_response200420_result_data_dict = inline_response200420_result_data_instance.to_dict()
# create an instance of InlineResponse200420ResultData from a dict
inline_response200420_result_data_from_dict = InlineResponse200420ResultData.from_dict(inline_response200420_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



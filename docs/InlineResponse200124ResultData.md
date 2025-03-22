# InlineResponse200124ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegates** | **List[str]** | An array of the mailing list&#39;s administrators. | [optional] 
**metadata** | [**InlineResponse200124ResultDataMetadata**](InlineResponse200124ResultDataMetadata.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200124_result_data import InlineResponse200124ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200124ResultData from a JSON string
inline_response200124_result_data_instance = InlineResponse200124ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200124ResultData.to_json())

# convert the object into a dict
inline_response200124_result_data_dict = inline_response200124_result_data_instance.to_dict()
# create an instance of InlineResponse200124ResultData from a dict
inline_response200124_result_data_from_dict = InlineResponse200124ResultData.from_dict(inline_response200124_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200264ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_data** | **str** | The GPG public key&#39;s contents. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200264_result_data import InlineResponse200264ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200264ResultData from a JSON string
inline_response200264_result_data_instance = InlineResponse200264ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200264ResultData.to_json())

# convert the object into a dict
inline_response200264_result_data_dict = inline_response200264_result_data_instance.to_dict()
# create an instance of InlineResponse200264ResultData from a dict
inline_response200264_result_data_from_dict = InlineResponse200264ResultData.from_dict(inline_response200264_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



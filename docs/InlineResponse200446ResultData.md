# InlineResponse200446ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**InlineResponse200446ResultDataDetails**](InlineResponse200446ResultDataDetails.md) |  | [optional] 
**text** | **str** | The raw information from the [OpenSSL](https://www.openssl.org/) command-line tool. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200446_result_data import InlineResponse200446ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200446ResultData from a JSON string
inline_response200446_result_data_instance = InlineResponse200446ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200446ResultData.to_json())

# convert the object into a dict
inline_response200446_result_data_dict = inline_response200446_result_data_instance.to_dict()
# create an instance of InlineResponse200446ResultData from a dict
inline_response200446_result_data_from_dict = InlineResponse200446ResultData.from_dict(inline_response200446_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



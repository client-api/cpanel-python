# InlineResponse200180ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The autoresponder&#39;s email address. | [optional] 
**subject** | **str** | The contents of the autoresponder message&#39;s &#x60;Subject:&#x60; field. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200180_result_data import InlineResponse200180ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200180ResultData from a JSON string
inline_response200180_result_data_instance = InlineResponse200180ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200180ResultData.to_json())

# convert the object into a dict
inline_response200180_result_data_dict = inline_response200180_result_data_instance.to_dict()
# create an instance of InlineResponse200180ResultData from a dict
inline_response200180_result_data_from_dict = InlineResponse200180ResultData.from_dict(inline_response200180_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



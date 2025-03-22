# InlineResponse200309ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The cPanel Market provider&#39;s display name. | [optional] 
**name** | **str** | The cPanel Market provider&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200309_result_data import InlineResponse200309ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200309ResultData from a JSON string
inline_response200309_result_data_instance = InlineResponse200309ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200309ResultData.to_json())

# convert the object into a dict
inline_response200309_result_data_dict = inline_response200309_result_data_instance.to_dict()
# create an instance of InlineResponse200309ResultData from a dict
inline_response200309_result_data_from_dict = InlineResponse200309ResultData.from_dict(inline_response200309_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20027ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The email message&#39;s contents. Up to the first 200 lines of an email message. | [optional] 
**contents** | **object** |  | [optional] 
**queuefile** | **str** | The message&#39;s filename. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20027_result_data import InlineResponse20027ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20027ResultData from a JSON string
inline_response20027_result_data_instance = InlineResponse20027ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20027ResultData.to_json())

# convert the object into a dict
inline_response20027_result_data_dict = inline_response20027_result_data_instance.to_dict()
# create an instance of InlineResponse20027ResultData from a dict
inline_response20027_result_data_from_dict = InlineResponse20027ResultData.from_dict(inline_response20027_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



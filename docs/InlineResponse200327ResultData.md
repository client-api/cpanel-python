# InlineResponse200327ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | **str** | The file extension. | [optional] 
**origin** | **str** | The handler&#39;s owner. *  &#x60;system&#x60; *  &#x60;user&#x60; | [optional] 
**type** | **str** | The MIME type. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200327_result_data import InlineResponse200327ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200327ResultData from a JSON string
inline_response200327_result_data_instance = InlineResponse200327ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200327ResultData.to_json())

# convert the object into a dict
inline_response200327_result_data_dict = inline_response200327_result_data_instance.to_dict()
# create an instance of InlineResponse200327ResultData from a dict
inline_response200327_result_data_from_dict = InlineResponse200327ResultData.from_dict(inline_response200327_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



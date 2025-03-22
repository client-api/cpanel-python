# InlineResponse200392ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The test message&#39;s ID. | [optional] 
**payload** | **object** | The payload from the Pushbullet server. For more information, read [Pushbullet&#39;s API documentation](https://docs.pushbullet.com/).  **Warning:**  This return may contain values that are Boolean primitives. JSON properly represents these, but XML represents them as &#x60;0&#x60; or &#x60;1&#x60;. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200392_result_data import InlineResponse200392ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200392ResultData from a JSON string
inline_response200392_result_data_instance = InlineResponse200392ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200392ResultData.to_json())

# convert the object into a dict
inline_response200392_result_data_dict = inline_response200392_result_data_instance.to_dict()
# create an instance of InlineResponse200392ResultData from a dict
inline_response200392_result_data_from_dict = InlineResponse200392ResultData.from_dict(inline_response200392_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



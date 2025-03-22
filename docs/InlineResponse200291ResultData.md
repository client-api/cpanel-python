# InlineResponse200291ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The locale&#39;s text direction. * &#x60;ltr&#x60; - left to right. * &#x60;rtl&#x60; - right to left. | [optional] 
**encoding** | **str** | The user&#39;s character set. | [optional] 
**locale** | **str** | The locale&#39;s two-letter ISO-3166 code. | [optional] 
**name** | **str** | The locale&#39;s full name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200291_result_data import InlineResponse200291ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200291ResultData from a JSON string
inline_response200291_result_data_instance = InlineResponse200291ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200291ResultData.to_json())

# convert the object into a dict
inline_response200291_result_data_dict = inline_response200291_result_data_instance.to_dict()
# create an instance of InlineResponse200291ResultData from a dict
inline_response200291_result_data_from_dict = InlineResponse200291ResultData.from_dict(inline_response200291_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200292ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The locale&#39;s text direction. * &#x60;ltr&#x60; - Left to right. * &#x60;rtl&#x60; - Right to left. | [optional] 
**local_name** | **str** | The locale&#39;s full name, in the locale&#39;s language. | [optional] 
**locale** | **str** | The locale&#39;s two-letter [ISO-3166 code](http://www.iso.org/iso/country_codes.htm). | [optional] 
**name** | **str** | The locale&#39;s full name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200292_result_data import InlineResponse200292ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200292ResultData from a JSON string
inline_response200292_result_data_instance = InlineResponse200292ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200292ResultData.to_json())

# convert the object into a dict
inline_response200292_result_data_dict = inline_response200292_result_data_instance.to_dict()
# create an instance of InlineResponse200292ResultData from a dict
inline_response200292_result_data_from_dict = InlineResponse200292ResultData.from_dict(inline_response200292_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



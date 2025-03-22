# InlineResponse200237ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **bytearray** | The file&#39;s contents. A string value.  **Note:**  Behavior is **undefined** if the calling context requires an encoding that conflicts with the file contents. For example, if the file contents are ISO-8859-1 but the context requires UTF-8 (as is the case with JSON), the system may apply an extra layer of UTF-8 encoding in order to satisfy the request. | [optional] 
**dir** | **str** | The absolute path to the directory that contains the selected file. | [optional] 
**filename** | **str** | The file&#39;s name. | [optional] 
**from_char** | **str** | The file&#39;s previous character encoding. If the request’s &#x60;from_charset&#x60; was &#x60;_DETECT_&#x60;, this will contain the detected encoding. Otherwise, it will contain the request’s &#x60;from_charset&#x60; value. | [optional] 
**from_charset** | **object** |  | [optional] 
**path** | **str** | The absolute path to the file. | [optional] 
**to_char** | **str** | The file&#39;s new character encoding. If the request’s &#x60;from_charset&#x60; was &#x60;_LOCALE_&#x60;, this will contain the locale’s encoding. Otherwise, it will contain the request’s &#x60;to_charset&#x60; value. | [optional] 
**to_charset** | **object** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200237_result_data import InlineResponse200237ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200237ResultData from a JSON string
inline_response200237_result_data_instance = InlineResponse200237ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200237ResultData.to_json())

# convert the object into a dict
inline_response200237_result_data_dict = inline_response200237_result_data_instance.to_dict()
# create an instance of InlineResponse200237ResultData from a dict
inline_response200237_result_data_from_dict = InlineResponse200237ResultData.from_dict(inline_response200237_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



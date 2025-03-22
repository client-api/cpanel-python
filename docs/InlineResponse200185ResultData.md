# InlineResponse200185ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest** | **str** | The forwarded address. | [optional] 
**forward** | **str** | The forwarded mail&#39;s destination. | [optional] 
**html_dest** | **str** | The forwarded address in an HTML-compatible format. | [optional] 
**html_forward** | **str** | The forwarded mail&#39;s destination in an HTML-compatible format. | [optional] 
**uri_dest** | **str** | The forwarded address in a URI-encoded format. | [optional] 
**uri_forward** | **str** | The forwarded mail&#39;s destination in a URI-encoded format. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200185_result_data import InlineResponse200185ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200185ResultData from a JSON string
inline_response200185_result_data_instance = InlineResponse200185ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200185ResultData.to_json())

# convert the object into a dict
inline_response200185_result_data_dict = inline_response200185_result_data_instance.to_dict()
# create an instance of InlineResponse200185ResultData from a dict
inline_response200185_result_data_from_dict = InlineResponse200185ResultData.from_dict(inline_response200185_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



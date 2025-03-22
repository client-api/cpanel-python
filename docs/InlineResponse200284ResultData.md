# InlineResponse200284ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directives** | [**List[InlineResponse200284ResultDataDirectives]**](InlineResponse200284ResultDataDirectives.md) | An array of the available directives in the &#x60;php.ini&#x60; file of the selected user&#39;s PHP version. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200284_result_data import InlineResponse200284ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200284ResultData from a JSON string
inline_response200284_result_data_instance = InlineResponse200284ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200284ResultData.to_json())

# convert the object into a dict
inline_response200284_result_data_dict = inline_response200284_result_data_instance.to_dict()
# create an instance of InlineResponse200284ResultData from a dict
inline_response200284_result_data_from_dict = InlineResponse200284ResultData.from_dict(inline_response200284_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



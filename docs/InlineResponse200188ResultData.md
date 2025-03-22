# InlineResponse200188ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain name. | [optional] 
**select** | **int** | The domain that you specified in the &#x60;select&#x60; input parameter. The function **only** returns this value if you included the &#x60;select&#x60; parameter when you called the function.  **Note:**    Because this value **only** appears if you included the &#x60;select&#x60; input parameter, The value **always** defaults to &#x60;1&#x60;. | [optional] [default to 1]

## Example

```python
from clientapi_cpanel.models.inline_response200188_result_data import InlineResponse200188ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200188ResultData from a JSON string
inline_response200188_result_data_instance = InlineResponse200188ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200188ResultData.to_json())

# convert the object into a dict
inline_response200188_result_data_dict = inline_response200188_result_data_instance.to_dict()
# create an instance of InlineResponse200188ResultData from a dict
inline_response200188_result_data_from_dict = InlineResponse200188ResultData.from_dict(inline_response200188_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



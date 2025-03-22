# InlineResponse20079ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_reason** | **str** | The reason that the DCV check failed. * &#x60;null&#x60; — The domain passed the DCV check. | [optional] 
**redirects** | [**List[InlineResponse20079ResultRedirects]**](InlineResponse20079ResultRedirects.md) | An array of objects that contains DCV check redirect information.  **Note:**   This **only** contains data if the &#x60;redirects_count&#x60; return includes a value greater than zero. | [optional] 
**redirects_count** | **int** | The number of HTTP redirects that the DCV check follows. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20079_result_data import InlineResponse20079ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20079ResultData from a JSON string
inline_response20079_result_data_instance = InlineResponse20079ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20079ResultData.to_json())

# convert the object into a dict
inline_response20079_result_data_dict = inline_response20079_result_data_instance.to_dict()
# create an instance of InlineResponse20079ResultData from a dict
inline_response20079_result_data_from_dict = InlineResponse20079ResultData.from_dict(inline_response20079_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



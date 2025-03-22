# InlineResponse200435ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **int** | Whether the system rebuilt the configuration files. * &#x60;1&#x60; - Configuration files rebuilt. * &#x60;0&#x60; - Configuration files **not** rebuilt. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200435_result_data import InlineResponse200435ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200435ResultData from a JSON string
inline_response200435_result_data_instance = InlineResponse200435ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200435ResultData.to_json())

# convert the object into a dict
inline_response200435_result_data_dict = inline_response200435_result_data_instance.to_dict()
# create an instance of InlineResponse200435ResultData from a dict
inline_response200435_result_data_from_dict = InlineResponse200435ResultData.from_dict(inline_response200435_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



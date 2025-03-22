# InlineResponse200485ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the test. | [optional] 
**rule_type** | **str** | The type and section of the email that the SpamAssassin analyses. * &#x60;body_tests&#x60; * &#x60;full_evals&#x60; * &#x60;head_evals&#x60; * &#x60;head_tests&#x60; * &#x60;meta_tests&#x60; * &#x60;other_tests&#x60; * &#x60;rawbody_tests&#x60; * &#x60;uri_tests&#x60; | [optional] 
**score** | [**InlineResponse200485ResultDataScore**](InlineResponse200485ResultDataScore.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200485_result_data import InlineResponse200485ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200485ResultData from a JSON string
inline_response200485_result_data_instance = InlineResponse200485ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200485ResultData.to_json())

# convert the object into a dict
inline_response200485_result_data_dict = inline_response200485_result_data_instance.to_dict()
# create an instance of InlineResponse200485ResultData from a dict
inline_response200485_result_data_from_dict = InlineResponse200485ResultData.from_dict(inline_response200485_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



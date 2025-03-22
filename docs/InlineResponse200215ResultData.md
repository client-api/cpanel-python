# InlineResponse200215ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for which the DMARC record was applied. | [optional] 
**msg** | **str** | The domain&#39;s DMARC record status message. | [optional] 
**status** | **int** | Whether the system applied a DMARC record to the domain. * &#x60;1&#x60; - Applied. * &#x60;0&#x60; - The system did **not** apply a DMARC record. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200215_result_data import InlineResponse200215ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200215ResultData from a JSON string
inline_response200215_result_data_instance = InlineResponse200215ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200215ResultData.to_json())

# convert the object into a dict
inline_response200215_result_data_dict = inline_response200215_result_data_instance.to_dict()
# create an instance of InlineResponse200215ResultData from a dict
inline_response200215_result_data_from_dict = InlineResponse200215ResultData.from_dict(inline_response200215_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



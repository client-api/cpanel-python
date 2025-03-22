# InlineResponse200222ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for which the DMARC record was removed. | [optional] 
**msg** | **str** | Information about the removed DMARC record. | [optional] 
**status** | **int** | Whether the system removed the domain&#39;s DMARC record. * &#x60;1&#x60; - The system removed the domain&#39;s DMARC record. * &#x60;0&#x60; - The system did **not** remove the domain&#39;s DMARC record. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200222_result_data import InlineResponse200222ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200222ResultData from a JSON string
inline_response200222_result_data_instance = InlineResponse200222ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200222ResultData.to_json())

# convert the object into a dict
inline_response200222_result_data_dict = inline_response200222_result_data_instance.to_dict()
# create an instance of InlineResponse200222ResultData from a dict
inline_response200222_result_data_from_dict = InlineResponse200222ResultData.from_dict(inline_response200222_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200433ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname. | [optional] 
**id** | **str** | The certificate&#39;s ID. | [optional] 
**type** | **str** | The type of SSL item. * &#x60;key&#x60; * &#x60;csr&#x60; * &#x60;crt&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200433_result_data import InlineResponse200433ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200433ResultData from a JSON string
inline_response200433_result_data_instance = InlineResponse200433ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200433ResultData.to_json())

# convert the object into a dict
inline_response200433_result_data_dict = inline_response200433_result_data_instance.to_dict()
# create an instance of InlineResponse200433ResultData from a dict
inline_response200433_result_data_from_dict = InlineResponse200433ResultData.from_dict(inline_response200433_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



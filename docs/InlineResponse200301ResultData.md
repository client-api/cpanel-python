# InlineResponse200301ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **int** | Whether the system changed mailbox name setting&#39;s status. * &#x60;1&#x60; - Success. * &#x60;0&#x60; - Failure. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200301_result_data import InlineResponse200301ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200301ResultData from a JSON string
inline_response200301_result_data_instance = InlineResponse200301ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200301ResultData.to_json())

# convert the object into a dict
inline_response200301_result_data_dict = inline_response200301_result_data_instance.to_dict()
# create an instance of InlineResponse200301ResultData from a dict
inline_response200301_result_data_from_dict = InlineResponse200301ResultData.from_dict(inline_response200301_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200400ResultData

An object containing the status of the operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **int** | Whether the &#x60;overwrite&#x60; parameter succeeded.  * &#x60;1&#x60; — Success. * &#x60;0&#x60; — Failure. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200400_result_data import InlineResponse200400ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200400ResultData from a JSON string
inline_response200400_result_data_instance = InlineResponse200400ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200400ResultData.to_json())

# convert the object into a dict
inline_response200400_result_data_dict = inline_response200400_result_data_instance.to_dict()
# create an instance of InlineResponse200400ResultData from a dict
inline_response200400_result_data_from_dict = InlineResponse200400ResultData.from_dict(inline_response200400_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



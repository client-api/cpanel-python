# InlineResponse200357ResultDataFailures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message. | [optional] 
**host** | **str** | The hostname that reported the error. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200357_result_data_failures import InlineResponse200357ResultDataFailures

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200357ResultDataFailures from a JSON string
inline_response200357_result_data_failures_instance = InlineResponse200357ResultDataFailures.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200357ResultDataFailures.to_json())

# convert the object into a dict
inline_response200357_result_data_failures_dict = inline_response200357_result_data_failures_instance.to_dict()
# create an instance of InlineResponse200357ResultDataFailures from a dict
inline_response200357_result_data_failures_from_dict = InlineResponse200357ResultDataFailures.from_dict(inline_response200357_result_data_failures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



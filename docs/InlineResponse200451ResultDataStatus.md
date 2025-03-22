# InlineResponse200451ResultDataStatus

Whether the resource is enabled or disabled.  * `1` — Enabled. * `0` — Disabled. * `unknown` — The system couldn't determine the resource's status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200451_result_data_status import InlineResponse200451ResultDataStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200451ResultDataStatus from a JSON string
inline_response200451_result_data_status_instance = InlineResponse200451ResultDataStatus.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200451ResultDataStatus.to_json())

# convert the object into a dict
inline_response200451_result_data_status_dict = inline_response200451_result_data_status_instance.to_dict()
# create an instance of InlineResponse200451ResultDataStatus from a dict
inline_response200451_result_data_status_from_dict = InlineResponse200451ResultDataStatus.from_dict(inline_response200451_result_data_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



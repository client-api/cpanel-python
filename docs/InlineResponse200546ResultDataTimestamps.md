# InlineResponse200546ResultDataTimestamps

A hash of timestamps for the deployment process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queued** | **str** | The time at which the deployment process. entered the task queue. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200546_result_data_timestamps import InlineResponse200546ResultDataTimestamps

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200546ResultDataTimestamps from a JSON string
inline_response200546_result_data_timestamps_instance = InlineResponse200546ResultDataTimestamps.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200546ResultDataTimestamps.to_json())

# convert the object into a dict
inline_response200546_result_data_timestamps_dict = inline_response200546_result_data_timestamps_instance.to_dict()
# create an instance of InlineResponse200546ResultDataTimestamps from a dict
inline_response200546_result_data_timestamps_from_dict = InlineResponse200546ResultDataTimestamps.from_dict(inline_response200546_result_data_timestamps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



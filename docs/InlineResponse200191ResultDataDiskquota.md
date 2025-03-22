# InlineResponse200191ResultDataDiskquota

The email account's disk quota. * A positive value that represents the email address's quota, in megabytes (MB). * `unlimited`, `∞`, or HTML code to display an infinity image - The email account has an unlimited quota.  **Note:**    The `infinityimg` and `infinitylang` parameters determine the unlimited value for this return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200191_result_data_diskquota import InlineResponse200191ResultDataDiskquota

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200191ResultDataDiskquota from a JSON string
inline_response200191_result_data_diskquota_instance = InlineResponse200191ResultDataDiskquota.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200191ResultDataDiskquota.to_json())

# convert the object into a dict
inline_response200191_result_data_diskquota_dict = inline_response200191_result_data_diskquota_instance.to_dict()
# create an instance of InlineResponse200191ResultDataDiskquota from a dict
inline_response200191_result_data_diskquota_from_dict = InlineResponse200191ResultDataDiskquota.from_dict(inline_response200191_result_data_diskquota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



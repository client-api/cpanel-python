# InlineResponse200254ResultDataDiskquota

The FTP account's quota.  * `unlimited` * The disk quota in megabytes, with two digits of fractional precision, encoded as a string.  **Note:**  This value is different from the value for `_diskquota`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200254_result_data_diskquota import InlineResponse200254ResultDataDiskquota

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200254ResultDataDiskquota from a JSON string
inline_response200254_result_data_diskquota_instance = InlineResponse200254ResultDataDiskquota.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200254ResultDataDiskquota.to_json())

# convert the object into a dict
inline_response200254_result_data_diskquota_dict = inline_response200254_result_data_diskquota_instance.to_dict()
# create an instance of InlineResponse200254ResultDataDiskquota from a dict
inline_response200254_result_data_diskquota_from_dict = InlineResponse200254ResultDataDiskquota.from_dict(inline_response200254_result_data_diskquota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200399ResultDataBackupID

The backup's identification.  * A date, in `YYYY-MM-DD` format. * `incremental` — An incremental daily backup. * The backup frequency (`weekly` or `monthly`) , a slash character (`/`), and the value `incremental`. * The backup frequency (`weekly` or `monthly`), a slash character (`/`), and the backup date, in `YYYY-MM-DD` format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200399_result_data_backup_id import InlineResponse200399ResultDataBackupID

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200399ResultDataBackupID from a JSON string
inline_response200399_result_data_backup_id_instance = InlineResponse200399ResultDataBackupID.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200399ResultDataBackupID.to_json())

# convert the object into a dict
inline_response200399_result_data_backup_id_dict = inline_response200399_result_data_backup_id_instance.to_dict()
# create an instance of InlineResponse200399ResultDataBackupID from a dict
inline_response200399_result_data_backup_id_from_dict = InlineResponse200399ResultDataBackupID.from_dict(inline_response200399_result_data_backup_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



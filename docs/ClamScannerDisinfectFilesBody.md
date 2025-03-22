# ClamScannerDisinfectFilesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **Dict[str, str]** | The user provides the actions to perform on each specific infected file found in the scan. | [optional] 

## Example

```python
from clientapi_cpanel.models.clam_scanner_disinfect_files_body import ClamScannerDisinfectFilesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClamScannerDisinfectFilesBody from a JSON string
clam_scanner_disinfect_files_body_instance = ClamScannerDisinfectFilesBody.from_json(json)
# print the JSON string representation of the object
print(ClamScannerDisinfectFilesBody.to_json())

# convert the object into a dict
clam_scanner_disinfect_files_body_dict = clam_scanner_disinfect_files_body_instance.to_dict()
# create an instance of ClamScannerDisinfectFilesBody from a dict
clam_scanner_disinfect_files_body_from_dict = ClamScannerDisinfectFilesBody.from_dict(clam_scanner_disinfect_files_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



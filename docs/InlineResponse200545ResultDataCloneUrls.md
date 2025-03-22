# InlineResponse200545ResultDataCloneUrls

An object containing the URLs to use to clone the repository.  The function returns an empty object if the account does **not** include the *Shell Access* setting.  **Important:**  If the server uses a nonstandard SSH port, the system returns a clone URL that includes the port number. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **List[str]** | A list of clone URLs with read-only permissions.  This function returns an empty list if the account does **not** include the *Shell Access* setting.  **Important:**  If the server uses a nonstandard SSH port, the system returns a clone URL that includes the port number. | [optional] 
**read_write** | **List[str]** | A list of clone URLs with read-write permissions.  This function returns an empty list if the account does **not** include the *Shell Access* setting.  **Important:**  If the server uses a nonstandard SSH port, the system returns a clone URL that includes the port number. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200545_result_data_clone_urls import InlineResponse200545ResultDataCloneUrls

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200545ResultDataCloneUrls from a JSON string
inline_response200545_result_data_clone_urls_instance = InlineResponse200545ResultDataCloneUrls.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200545ResultDataCloneUrls.to_json())

# convert the object into a dict
inline_response200545_result_data_clone_urls_dict = inline_response200545_result_data_clone_urls_instance.to_dict()
# create an instance of InlineResponse200545ResultDataCloneUrls from a dict
inline_response200545_result_data_clone_urls_from_dict = InlineResponse200545ResultDataCloneUrls.from_dict(inline_response200545_result_data_clone_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200542ResultDataCloneUrls

An object containing URLs to use to clone the repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **List[str]** | A list of clone URLs with read-only permissions. The function returns a blank array if the account does **not** include the *Shell Access* setting.  **Important:**  If the server uses a [nonstandard SSH port](https://go.cpanel.net/firewall), the system returns a clone URL that includes the port number. | [optional] 
**read_write** | **List[str]** | A list of of clone URLs with read-write permissions. The function returns a blank array if the account does **not** include the *Shell Access* setting.  **Important:**  If the server uses a [nonstandard SSH port](https://go.cpanel.net/firewall), the system returns a clone URL that includes the port number. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200542_result_data_clone_urls import InlineResponse200542ResultDataCloneUrls

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200542ResultDataCloneUrls from a JSON string
inline_response200542_result_data_clone_urls_instance = InlineResponse200542ResultDataCloneUrls.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200542ResultDataCloneUrls.to_json())

# convert the object into a dict
inline_response200542_result_data_clone_urls_dict = inline_response200542_result_data_clone_urls_instance.to_dict()
# create an instance of InlineResponse200542ResultDataCloneUrls from a dict
inline_response200542_result_data_clone_urls_from_dict = InlineResponse200542ResultDataCloneUrls.from_dict(inline_response200542_result_data_clone_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



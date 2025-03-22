# InlineResponse200567ResultDataAdmins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user&#39;s automatically generated identifier. | [optional] 
**display_name** | **str** | The user&#39;s display name. | [optional] 
**user_email** | **str** | The user&#39;s email address. | [optional] 
**user_login** | **str** | The user&#39;s login name. | [optional] 
**user_nicename** | **str** | The user&#39;s simplified username, which you can use as an HTML ID or similar. | [optional] 
**user_status** | **int** | The user&#39;s verified status. * &#x60;1&#x60; — Verified. * &#x60;0&#x60; — Unverified. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200567_result_data_admins import InlineResponse200567ResultDataAdmins

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200567ResultDataAdmins from a JSON string
inline_response200567_result_data_admins_instance = InlineResponse200567ResultDataAdmins.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200567ResultDataAdmins.to_json())

# convert the object into a dict
inline_response200567_result_data_admins_dict = inline_response200567_result_data_admins_instance.to_dict()
# create an instance of InlineResponse200567ResultDataAdmins from a dict
inline_response200567_result_data_admins_from_dict = InlineResponse200567ResultDataAdmins.from_dict(inline_response200567_result_data_admins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



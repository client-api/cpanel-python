# InlineResponse200460ResultData

An object that contains user attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_token** | **str** | The long-lived token for this account. The &lt;a href&#x3D;\&quot;https://go.cpanel.net/5k\&quot; target&#x3D;\&quot;_blank\&quot;&gt;koality&lt;/a&gt; servers require this token to authenticate. If this token is lost, the user must create a new account. | [optional] 
**username** | **str** | The account&#39;s username. This value reflects the &#x60;email&#x60; parameter. | [optional] 
**enabled** | **bool** | Whether the account is enabled to process user data.  * &#x60;false&#x60; - The account is disabled.  * &#x60;true&#x60; - The account is enabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200460_result_data import InlineResponse200460ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200460ResultData from a JSON string
inline_response200460_result_data_instance = InlineResponse200460ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200460ResultData.to_json())

# convert the object into a dict
inline_response200460_result_data_dict = inline_response200460_result_data_instance.to_dict()
# create an instance of InlineResponse200460ResultData from a dict
inline_response200460_result_data_from_dict = InlineResponse200460ResultData.from_dict(inline_response200460_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



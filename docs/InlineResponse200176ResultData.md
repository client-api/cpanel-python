# InlineResponse200176ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The email account&#39;s mail server hostname. | [optional] 
**has_maildir** | **int** | Whether &#x60;Maildir&#x60; is enabled for the email account.  * &#x60;1&#x60; — Enabled.  It is not possible to disable &#x60;Maildir&#x60;. | [optional] 
**user** | [**InlineResponse200176ResultDataUser**](InlineResponse200176ResultDataUser.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200176_result_data import InlineResponse200176ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200176ResultData from a JSON string
inline_response200176_result_data_instance = InlineResponse200176ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200176ResultData.to_json())

# convert the object into a dict
inline_response200176_result_data_dict = inline_response200176_result_data_instance.to_dict()
# create an instance of InlineResponse200176ResultData from a dict
inline_response200176_result_data_from_dict = InlineResponse200176ResultData.from_dict(inline_response200176_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



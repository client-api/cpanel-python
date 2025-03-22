# InlineResponse200300ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the user currently uses UTF-8 character-encoded mailbox names. * &#x60;1&#x60; - Uses UTF-8 character-encoded mailbox names. * &#x60;0&#x60; - Does **not** use UTF-8 character-encoded mailbox names. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200300_result_data import InlineResponse200300ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200300ResultData from a JSON string
inline_response200300_result_data_instance = InlineResponse200300ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200300ResultData.to_json())

# convert the object into a dict
inline_response200300_result_data_dict = inline_response200300_result_data_instance.to_dict()
# create an instance of InlineResponse200300ResultData from a dict
inline_response200300_result_data_from_dict = InlineResponse200300ResultData.from_dict(inline_response200300_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



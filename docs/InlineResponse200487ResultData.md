# InlineResponse200487ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **List[str]** | An array containing custom SpamAssassin variable values.  **Note:**  The array&#39;s name is the custom SpamAssassin variable&#39;s name. | [optional] 
**blacklist_from** | **List[str]** | An array of email addresses on the blacklist. | [optional] 
**required_score** | **List[float]** | An array containing the score at which the system will mark a message as spam. The system considers mail that matches this score to be spam. | [optional] 
**score** | **List[str]** | An array of the symbolic test names and their scores. | [optional] 
**whitelist_from** | **List[str]** | An array of the email addresses on the whitelist. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200487_result_data import InlineResponse200487ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200487ResultData from a JSON string
inline_response200487_result_data_instance = InlineResponse200487ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200487ResultData.to_json())

# convert the object into a dict
inline_response200487_result_data_dict = inline_response200487_result_data_instance.to_dict()
# create an instance of InlineResponse200487ResultData from a dict
inline_response200487_result_data_from_dict = InlineResponse200487ResultData.from_dict(inline_response200487_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



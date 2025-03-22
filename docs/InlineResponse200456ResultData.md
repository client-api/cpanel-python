# InlineResponse200456ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The Webmail server&#39;s hostname.  **Note:**  The function returns a &#x60;null&#x60; value when the Webmail server is not remote. | [optional] 
**session** | **str** | The session ID to submit via POST to begin using the new session. | [optional] 
**token** | **str** | A new security token. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200456_result_data import InlineResponse200456ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200456ResultData from a JSON string
inline_response200456_result_data_instance = InlineResponse200456ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200456ResultData.to_json())

# convert the object into a dict
inline_response200456_result_data_dict = inline_response200456_result_data_instance.to_dict()
# create an instance of InlineResponse200456ResultData from a dict
inline_response200456_result_data_from_dict = InlineResponse200456ResultData.from_dict(inline_response200456_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



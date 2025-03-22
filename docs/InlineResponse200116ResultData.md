# InlineResponse200116ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **int** | The DDNS domain’s creation time. | [optional] 
**description** | **str** | A user-editable string that describes the DDNS domain. | [optional] 
**domain** | **str** | The domain. | [optional] 
**id** | **str** | The domain’s DDNS ID.  **Note:**  This ID goes into the URL that the client uses to [update the domain’s IP address resolution](https://go.cpanel.net/cpaneldocsdynamicdns). | [optional] 
**last_run_times** | **List[int]** | The most recent times when the web call ran.  **Note:**  This list changes every time the web call runs, even if the domain’s IP address resolution does **not** change. | [optional] 
**last_update_time** | **int** | The most recent update time for the DDNS domain.  **Note:**  This value changes **only** when the domain’s IP address resolution changes. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200116_result_data import InlineResponse200116ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200116ResultData from a JSON string
inline_response200116_result_data_instance = InlineResponse200116ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200116ResultData.to_json())

# convert the object into a dict
inline_response200116_result_data_dict = inline_response200116_result_data_instance.to_dict()
# create an instance of InlineResponse200116ResultData from a dict
inline_response200116_result_data_from_dict = InlineResponse200116ResultData.from_dict(inline_response200116_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



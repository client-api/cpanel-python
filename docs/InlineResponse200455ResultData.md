# InlineResponse200455ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | Whether the function successfully created the temporary user session. * &#x60;1&#x60; - Success. * &#x60;0&#x60; - Failure. | [optional] 
**session_temp_user** | **str** | The temporary user&#39;s session ID. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200455_result_data import InlineResponse200455ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200455ResultData from a JSON string
inline_response200455_result_data_instance = InlineResponse200455ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200455ResultData.to_json())

# convert the object into a dict
inline_response200455_result_data_dict = inline_response200455_result_data_instance.to_dict()
# create an instance of InlineResponse200455ResultData from a dict
inline_response200455_result_data_from_dict = InlineResponse200455ResultData.from_dict(inline_response200455_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



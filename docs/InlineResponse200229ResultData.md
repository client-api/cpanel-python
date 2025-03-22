# InlineResponse200229ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_time** | **int** | When the user linked their account to the identity provider. | [optional] 
**preferred_username** | **str** | The preferred username of the account on the identity provider. | [optional] 
**provider_id** | **str** | The system&#39;s unique key for the identity provider. | [optional] 
**provider_protocol** | **str** | The identity provider&#39;s protocol. | [optional] 
**subject_unique_identifier** | **int** | The unique identifier for the user at the identity provider. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200229_result_data import InlineResponse200229ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200229ResultData from a JSON string
inline_response200229_result_data_instance = InlineResponse200229ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200229ResultData.to_json())

# convert the object into a dict
inline_response200229_result_data_dict = inline_response200229_result_data_instance.to_dict()
# create an instance of InlineResponse200229ResultData from a dict
inline_response200229_result_data_from_dict = InlineResponse200229ResultData.from_dict(inline_response200229_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



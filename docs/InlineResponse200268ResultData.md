# InlineResponse200268ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The key&#39;s algorithm. * RSA * DSA | [optional] 
**bits** | **int** | The length of the key, in bits. | [optional] 
**created** | **str** | The creation time for the key, in [Unix time format](http://en.wikipedia.org/wiki/Unix_time). | [optional] 
**expires** | **str** | When the key will expire, in [Unix time format](http://en.wikipedia.org/wiki/Unix_time).  **Note:**  If the key does not expire, this will be an empty string. | [optional] 
**id** | **str** | The key&#39;s ID. | [optional] 
**type** | **str** | The type of key.  **Note:**  This will always be \&quot;pub\&quot; because we are listing public keys. | [optional] 
**user_id** | **str** | The user ID of the key which consists of the following space-separated values: * The username. * The key&#39;s comment in parentheses. * The key&#39;s email address in angle brackets (&lt;&gt;). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200268_result_data import InlineResponse200268ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200268ResultData from a JSON string
inline_response200268_result_data_instance = InlineResponse200268ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200268ResultData.to_json())

# convert the object into a dict
inline_response200268_result_data_dict = inline_response200268_result_data_instance.to_dict()
# create an instance of InlineResponse200268ResultData from a dict
inline_response200268_result_data_from_dict = InlineResponse200268ResultData.from_dict(inline_response200268_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



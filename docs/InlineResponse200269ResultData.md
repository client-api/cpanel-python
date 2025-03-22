# InlineResponse200269ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The key&#39;s algorithm. * &#x60;RSA&#x60; * &#x60;DSA&#x60; | [optional] 
**bits** | **int** | The key&#39;s length. | [optional] 
**created** | **int** | When the function created the key. | [optional] 
**expires** | **int** | When the key will expire. | [optional] 
**id** | **str** | The key&#39;s ID. | [optional] 
**type** | **str** | The type of key.  * &#x60;sec&#x60; is the only possible value. | [optional] 
**user_id** | **str** | The user ID of the key. The system returns this value as a space-separated string with the following values:  * The username. * A comment in parentheses. * The key&#39;s email address in angle brackets (&#x60;&lt;&gt;&#x60;). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200269_result_data import InlineResponse200269ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200269ResultData from a JSON string
inline_response200269_result_data_instance = InlineResponse200269ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200269ResultData.to_json())

# convert the object into a dict
inline_response200269_result_data_dict = inline_response200269_result_data_instance.to_dict()
# create an instance of InlineResponse200269ResultData from a dict
inline_response200269_result_data_from_dict = InlineResponse200269ResultData.from_dict(inline_response200269_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20096ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for which the system imported the zone key. | [optional] 
**error** | **str** | An error message that describes why the system could not import the security key.  **Note:**  The function **only** displays this return when the &#x60;success&#x60; return is a &#x60;0&#x60; value. | [optional] 
**new_key_id** | **str** | The security key&#39;s ID. | [optional] 
**success** | **int** | Whether the system imported the security key.  * &#x60;1&#x60; - The system imported the security key. * &#x60;0&#x60; - The system **failed** to import the security key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20096_result_data import InlineResponse20096ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20096ResultData from a JSON string
inline_response20096_result_data_instance = InlineResponse20096ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20096ResultData.to_json())

# convert the object into a dict
inline_response20096_result_data_dict = inline_response20096_result_data_instance.to_dict()
# create an instance of InlineResponse20096ResultData from a dict
inline_response20096_result_data_from_dict = InlineResponse20096ResultData.from_dict(inline_response20096_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



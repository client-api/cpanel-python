# InlineResponse20090ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for which the system deactivated a security key. | [optional] 
**error** | **str** | An error message that describes why the system could not deactivate the security key.  **Note**  The function **only** displays this return when the &#x60;success&#x60; return is a &#x60;0&#x60; value. | [optional] 
**key_id** | **str** | The security key&#39;s ID. | [optional] 
**success** | **int** | Whether the system deactivated the security key.  * &#x60;1&#x60; - Deactivated. * &#x60;0&#x60; - The system failed to deactivate the security key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20090_result_data import InlineResponse20090ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20090ResultData from a JSON string
inline_response20090_result_data_instance = InlineResponse20090ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20090ResultData.to_json())

# convert the object into a dict
inline_response20090_result_data_dict = inline_response20090_result_data_instance.to_dict()
# create an instance of InlineResponse20090ResultData from a dict
inline_response20090_result_data_from_dict = InlineResponse20090ResultData.from_dict(inline_response20090_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



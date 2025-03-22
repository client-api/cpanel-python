# InlineResponse200524ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tfa_removed** | **int** | Whether the system removed the user from the two-factor authentication &#x60;userdata&#x60; file. * &#x60;1&#x60; - Removed.  **Note:**  If a removal fails, the system sends a failure response with the reason in the metadata. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200524_result_data import InlineResponse200524ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200524ResultData from a JSON string
inline_response200524_result_data_instance = InlineResponse200524ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200524ResultData.to_json())

# convert the object into a dict
inline_response200524_result_data_dict = inline_response200524_result_data_instance.to_dict()
# create an instance of InlineResponse200524ResultData from a dict
inline_response200524_result_data_from_dict = InlineResponse200524ResultData.from_dict(inline_response200524_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



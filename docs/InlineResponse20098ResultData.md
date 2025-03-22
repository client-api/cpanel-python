# InlineResponse20098ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Dict[str, int]** | Contains the domains for which the system enabled NSEC3.  **Note:**  This return&#39;s name is the &#x60;domain&#x60; parameter&#39;s value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20098_result_data import InlineResponse20098ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20098ResultData from a JSON string
inline_response20098_result_data_instance = InlineResponse20098ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20098ResultData.to_json())

# convert the object into a dict
inline_response20098_result_data_dict = inline_response20098_result_data_instance.to_dict()
# create an instance of InlineResponse20098ResultData from a dict
inline_response20098_result_data_from_dict = InlineResponse20098ResultData.from_dict(inline_response20098_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



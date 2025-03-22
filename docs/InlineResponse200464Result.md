# InlineResponse200464Result


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InlineResponse200464ResultData**](InlineResponse200464ResultData.md) |  | [optional] 
**errors** | **List[str]** | List of errors if the API failed. | [optional] 
**messages** | **List[str]** | List of messages the API generated. | [optional] 
**metadata** | **object** |  | [optional] 
**status** | **int** | * &#x60;1&#x60; — Success. * &#x60;0&#x60; — Failed. Check the &#x60;errors&#x60; field for more details. | [optional] 
**warnings** | **List[str]** | List of warnings that the API generated. Warnings describe non-critical failures or issues the system noted while running an API function. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200464_result import InlineResponse200464Result

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200464Result from a JSON string
inline_response200464_result_instance = InlineResponse200464Result.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200464Result.to_json())

# convert the object into a dict
inline_response200464_result_dict = inline_response200464_result_instance.to_dict()
# create an instance of InlineResponse200464Result from a dict
inline_response200464_result_from_dict = InlineResponse200464Result.from_dict(inline_response200464_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



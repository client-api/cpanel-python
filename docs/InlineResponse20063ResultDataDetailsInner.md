# InlineResponse20063ResultDataDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The absolute path to the file. | [optional] 
**id** | **float** | The task processing order. | [optional] 
**message** | **str** | Optional message that may include more information about errors. | [optional] 
**state** | **str** | The state of the step. It will be one of the following:  * &#x60;error&#x60; - An error occurred while processing the file. * &#x60;info&#x60; - The message is information only. * &#x60;success&#x60; - The disinfection was successful. | 
**type** | **str** | * &#x60;step&#x60; - Record about a single file being processes. | 

## Example

```python
from clientapi_cpanel.models.inline_response20063_result_data_details_inner import InlineResponse20063ResultDataDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20063ResultDataDetailsInner from a JSON string
inline_response20063_result_data_details_inner_instance = InlineResponse20063ResultDataDetailsInner.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20063ResultDataDetailsInner.to_json())

# convert the object into a dict
inline_response20063_result_data_details_inner_dict = inline_response20063_result_data_details_inner_instance.to_dict()
# create an instance of InlineResponse20063ResultDataDetailsInner from a dict
inline_response20063_result_data_details_inner_from_dict = InlineResponse20063ResultDataDetailsInner.from_dict(inline_response20063_result_data_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



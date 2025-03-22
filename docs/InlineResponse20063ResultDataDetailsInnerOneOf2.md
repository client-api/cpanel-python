# InlineResponse20063ResultDataDetailsInnerOneOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The task processing order. | [optional] 
**message** | **str** | Optional message that may include more information about errors. | [optional] 
**state** | **str** | The state of the step. It will be one of the following:  * &#x60;error&#x60; - An error occurred while processing the file. * &#x60;info&#x60; - The message is information only. * &#x60;success&#x60; - The disinfection was successful. | [optional] 
**type** | **str** | * &#x60;done&#x60; - Record that the disinfection is complete for all files indicated. | 

## Example

```python
from clientapi_cpanel.models.inline_response20063_result_data_details_inner_one_of2 import InlineResponse20063ResultDataDetailsInnerOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf2 from a JSON string
inline_response20063_result_data_details_inner_one_of2_instance = InlineResponse20063ResultDataDetailsInnerOneOf2.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20063ResultDataDetailsInnerOneOf2.to_json())

# convert the object into a dict
inline_response20063_result_data_details_inner_one_of2_dict = inline_response20063_result_data_details_inner_one_of2_instance.to_dict()
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf2 from a dict
inline_response20063_result_data_details_inner_one_of2_from_dict = InlineResponse20063ResultDataDetailsInnerOneOf2.from_dict(inline_response20063_result_data_details_inner_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20063ResultDataDetailsInnerOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The task processing order. | [optional] 
**message** | **str** | Optional message that may include more information about errors and warnings. | [optional] 
**state** | **str** | The state of the issue. It will be one of the following:  * &#x60;error&#x60; - An error occurred while starting or finishing the disinfection. * &#x60;warning&#x60; - A non-cricitcal problem occurred while starting or finishing the disinfection. | 
**type** | **str** | * &#x60;issue&#x60; - Record that the disinfection is complete for all files indicated. | 

## Example

```python
from clientapi_cpanel.models.inline_response20063_result_data_details_inner_one_of1 import InlineResponse20063ResultDataDetailsInnerOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf1 from a JSON string
inline_response20063_result_data_details_inner_one_of1_instance = InlineResponse20063ResultDataDetailsInnerOneOf1.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20063ResultDataDetailsInnerOneOf1.to_json())

# convert the object into a dict
inline_response20063_result_data_details_inner_one_of1_dict = inline_response20063_result_data_details_inner_one_of1_instance.to_dict()
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf1 from a dict
inline_response20063_result_data_details_inner_one_of1_from_dict = InlineResponse20063ResultDataDetailsInnerOneOf1.from_dict(inline_response20063_result_data_details_inner_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



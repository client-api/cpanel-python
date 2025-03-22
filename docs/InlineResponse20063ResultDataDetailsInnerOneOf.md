# InlineResponse20063ResultDataDetailsInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The absolute path to the file. | [optional] 
**id** | **float** | The task processing order. | [optional] 
**message** | **str** | Optional message that may include more information about errors. | [optional] 
**state** | **str** | The state of the step. It will be one of the following:  * &#x60;deleted&#x60; - The file was deleted. * &#x60;error&#x60; - An error occurred while processing the file. * &#x60;mailbox-cleansed&#x60; - The mailbox was clear of viruses. * &#x60;no-action&#x60; - No action was taken on the file. * &#x60;quarantined&#x60; - The file was quarantined. | 
**type** | **str** | * &#x60;step&#x60; - Record about a single file being processes. | 

## Example

```python
from clientapi_cpanel.models.inline_response20063_result_data_details_inner_one_of import InlineResponse20063ResultDataDetailsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf from a JSON string
inline_response20063_result_data_details_inner_one_of_instance = InlineResponse20063ResultDataDetailsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20063ResultDataDetailsInnerOneOf.to_json())

# convert the object into a dict
inline_response20063_result_data_details_inner_one_of_dict = inline_response20063_result_data_details_inner_one_of_instance.to_dict()
# create an instance of InlineResponse20063ResultDataDetailsInnerOneOf from a dict
inline_response20063_result_data_details_inner_one_of_from_dict = InlineResponse20063ResultDataDetailsInnerOneOf.from_dict(inline_response20063_result_data_details_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200586ResultCPGreyList

An object that contains the number of domains with Greylisting enabled or disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_disabled** | **int** | The number of domains with Greylisting disabled. | [optional] 
**total_enabled** | **int** | The number of domains with Greylisting enabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200586_result_cp_grey_list import InlineResponse200586ResultCPGreyList

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200586ResultCPGreyList from a JSON string
inline_response200586_result_cp_grey_list_instance = InlineResponse200586ResultCPGreyList.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200586ResultCPGreyList.to_json())

# convert the object into a dict
inline_response200586_result_cp_grey_list_dict = inline_response200586_result_cp_grey_list_instance.to_dict()
# create an instance of InlineResponse200586ResultCPGreyList from a dict
inline_response200586_result_cp_grey_list_from_dict = InlineResponse200586ResultCPGreyList.from_dict(inline_response200586_result_cp_grey_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



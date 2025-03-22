# InlineResponse200577ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **object** | Detailed information of the WordPress site. | [optional] 
**install_status** | **str** | Installation status of the WordPress site. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200577_result_data import InlineResponse200577ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200577ResultData from a JSON string
inline_response200577_result_data_instance = InlineResponse200577ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200577ResultData.to_json())

# convert the object into a dict
inline_response200577_result_data_dict = inline_response200577_result_data_instance.to_dict()
# create an instance of InlineResponse200577ResultData from a dict
inline_response200577_result_data_from_dict = InlineResponse200577ResultData.from_dict(inline_response200577_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



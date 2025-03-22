# InlineResponse200377ResultData

An object that contains information about the plugin's promotions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_show_promotions** | **int** | Whether the plugin can show promotions. * &#x60;1&#x60; — Can show promotions. * &#x60;0&#x60; — Can not show promotions. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200377_result_data import InlineResponse200377ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200377ResultData from a JSON string
inline_response200377_result_data_instance = InlineResponse200377ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200377ResultData.to_json())

# convert the object into a dict
inline_response200377_result_data_dict = inline_response200377_result_data_instance.to_dict()
# create an instance of InlineResponse200377ResultData from a dict
inline_response200377_result_data_from_dict = InlineResponse200377ResultData.from_dict(inline_response200377_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



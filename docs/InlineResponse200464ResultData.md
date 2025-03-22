# InlineResponse200464ResultData

An object that contains Site Quality Monitoring user attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_site_quality_user** | **int** | Whether the cPanel user has an associated Site Quality Monitoring account. * &#x60;1&#x60; - The user does have an associated account. * &#x60;0&#x60; - The user does not have an associated account. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200464_result_data import InlineResponse200464ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200464ResultData from a JSON string
inline_response200464_result_data_instance = InlineResponse200464ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200464ResultData.to_json())

# convert the object into a dict
inline_response200464_result_data_dict = inline_response200464_result_data_instance.to_dict()
# create an instance of InlineResponse200464ResultData from a dict
inline_response200464_result_data_from_dict = InlineResponse200464ResultData.from_dict(inline_response200464_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



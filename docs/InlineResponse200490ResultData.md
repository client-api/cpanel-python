# InlineResponse200490ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_domains** | **int** | Whether the statistics file&#39;s filepath is for all the domains on a cPanel account. * &#x60;1&#x60; - All domains. * &#x60;0&#x60; - An individual domain. | [optional] 
**domain** | **str** | The domain for which to display statistics. | [optional] 
**path** | **str** | The filepath to the statistics file. | [optional] 
**ssl** | **int** | Whether the function generates statistics from SSL requests. * &#x60;1&#x60; - Generates statistics for SSL requests. * &#x60;0&#x60; - Generates statistics for non-SSL requests. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200490_result_data import InlineResponse200490ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200490ResultData from a JSON string
inline_response200490_result_data_instance = InlineResponse200490ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200490ResultData.to_json())

# convert the object into a dict
inline_response200490_result_data_dict = inline_response200490_result_data_instance.to_dict()
# create an instance of InlineResponse200490ResultData from a dict
inline_response200490_result_data_from_dict = InlineResponse200490ResultData.from_dict(inline_response200490_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



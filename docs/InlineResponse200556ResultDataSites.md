# InlineResponse200556ResultDataSites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The WordPress site&#39;s unique ID.  **Note:**  &#x60;null&#x60; is the only possible value. We have not implemented this return. | [optional] 
**site** | **str** | The WordPress site&#39;s URL. The URL does not contain a protocol prefix. | [optional] 
**type** | **str** | The type of process that is active.  **Note:**  &#x60;backup&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200556_result_data_sites import InlineResponse200556ResultDataSites

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200556ResultDataSites from a JSON string
inline_response200556_result_data_sites_instance = InlineResponse200556ResultDataSites.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200556ResultDataSites.to_json())

# convert the object into a dict
inline_response200556_result_data_sites_dict = inline_response200556_result_data_sites_instance.to_dict()
# create an instance of InlineResponse200556ResultDataSites from a dict
inline_response200556_result_data_sites_from_dict = InlineResponse200556ResultDataSites.from_dict(inline_response200556_result_data_sites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



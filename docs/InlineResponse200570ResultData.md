# InlineResponse200570ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[InlineResponse200570ResultDataInstances]**](InlineResponse200570ResultDataInstances.md) | An array of objects that contains the WordPress instance information. | [optional] 
**is_running** | **int** | Whether the system detects an active scan.  * &#x60;1&#x60; - A scan is active. * &#x60;0&#x60; - No scans are active. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200570_result_data import InlineResponse200570ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200570ResultData from a JSON string
inline_response200570_result_data_instance = InlineResponse200570ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200570ResultData.to_json())

# convert the object into a dict
inline_response200570_result_data_dict = inline_response200570_result_data_instance.to_dict()
# create an instance of InlineResponse200570ResultData from a dict
inline_response200570_result_data_from_dict = InlineResponse200570ResultData.from_dict(inline_response200570_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



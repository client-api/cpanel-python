# InlineResponse20012ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | The interval in which the system reports bandwidth data. - &#x60;daily&#x60; - &#x60;hourly&#x60; - &#x60;5min&#x60; | [optional] 
**retention** | **int** | The retention period for bandwidth data. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20012_result_data import InlineResponse20012ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20012ResultData from a JSON string
inline_response20012_result_data_instance = InlineResponse20012ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20012ResultData.to_json())

# convert the object into a dict
inline_response20012_result_data_dict = inline_response20012_result_data_instance.to_dict()
# create an instance of InlineResponse20012ResultData from a dict
inline_response20012_result_data_from_dict = InlineResponse20012ResultData.from_dict(inline_response20012_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



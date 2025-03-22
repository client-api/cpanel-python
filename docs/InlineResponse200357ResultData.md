# InlineResponse200357ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[InlineResponse200357ResultDataFailures]**](InlineResponse200357ResultDataFailures.md) | An array of the function&#39;s error messages. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200357_result_data import InlineResponse200357ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200357ResultData from a JSON string
inline_response200357_result_data_instance = InlineResponse200357ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200357ResultData.to_json())

# convert the object into a dict
inline_response200357_result_data_dict = inline_response200357_result_data_instance.to_dict()
# create an instance of InlineResponse200357ResultData from a dict
inline_response200357_result_data_from_dict = InlineResponse200357ResultData.from_dict(inline_response200357_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



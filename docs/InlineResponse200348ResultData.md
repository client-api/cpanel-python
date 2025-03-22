# InlineResponse200348ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**InlineResponse200348ResultDataHost**](InlineResponse200348ResultDataHost.md) |  | [optional] 
**is_remote** | **int** | Whether the host is a remote MySQL server. * &#x60;1&#x60; - Remote host. * &#x60;0&#x60; - Local host. | [optional] 
**version** | **str** | The MySQL server&#39;s version. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200348_result_data import InlineResponse200348ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200348ResultData from a JSON string
inline_response200348_result_data_instance = InlineResponse200348ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200348ResultData.to_json())

# convert the object into a dict
inline_response200348_result_data_dict = inline_response200348_result_data_instance.to_dict()
# create an instance of InlineResponse200348ResultData from a dict
inline_response200348_result_data_from_dict = InlineResponse200348ResultData.from_dict(inline_response200348_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



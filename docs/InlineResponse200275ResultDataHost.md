# InlineResponse200275ResultDataHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**InlineResponse200275ResultDataHostHost**](InlineResponse200275ResultDataHostHost.md) |  | [optional] 
**key** | **str** | The host&#39;s key. | [optional] 
**line** | **str** | The host&#39;s entry in the &#x60;/home/user/.ssh/known_hosts&#x60; file, where &#x60;user&#x60; is the cPanel account username. | [optional] 
**meta** | [**InlineResponse200275ResultDataMeta**](InlineResponse200275ResultDataMeta.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200275_result_data_host import InlineResponse200275ResultDataHost

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200275ResultDataHost from a JSON string
inline_response200275_result_data_host_instance = InlineResponse200275ResultDataHost.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200275ResultDataHost.to_json())

# convert the object into a dict
inline_response200275_result_data_host_dict = inline_response200275_result_data_host_instance.to_dict()
# create an instance of InlineResponse200275ResultDataHost from a dict
inline_response200275_result_data_host_from_dict = InlineResponse200275ResultDataHost.from_dict(inline_response200275_result_data_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200278ResultDataHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**InlineResponse200278ResultDataHostHost**](InlineResponse200278ResultDataHostHost.md) |  | [optional] 
**key** | **str** | The host&#39;s key. | [optional] 
**line** | **str** | The host&#39;s entry in the &#x60;/home/user/.ssh/known_hosts&#x60; file, where &#x60;user&#x60; is the cPanel account username. | [optional] 
**meta** | [**InlineResponse200278ResultDataMeta**](InlineResponse200278ResultDataMeta.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200278_result_data_host import InlineResponse200278ResultDataHost

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200278ResultDataHost from a JSON string
inline_response200278_result_data_host_instance = InlineResponse200278ResultDataHost.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200278ResultDataHost.to_json())

# convert the object into a dict
inline_response200278_result_data_host_dict = inline_response200278_result_data_host_instance.to_dict()
# create an instance of InlineResponse200278ResultDataHost from a dict
inline_response200278_result_data_host_from_dict = InlineResponse200278ResultDataHost.from_dict(inline_response200278_result_data_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



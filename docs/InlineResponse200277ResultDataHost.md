# InlineResponse200277ResultDataHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**InlineResponse200277ResultDataHostHost**](InlineResponse200277ResultDataHostHost.md) |  | [optional] 
**key** | **str** | The host&#39;s key. | [optional] 
**line** | **str** | The host&#39;s entry in the &#x60;/home/user/.ssh/known_hosts&#x60; file, where user is the cPanel account username. A valid entry that includes the hostname or IP address, the key&#39;s algorithm, and the public key. | [optional] 
**meta** | [**InlineResponse200277ResultDataMeta**](InlineResponse200277ResultDataMeta.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200277_result_data_host import InlineResponse200277ResultDataHost

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200277ResultDataHost from a JSON string
inline_response200277_result_data_host_instance = InlineResponse200277ResultDataHost.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200277ResultDataHost.to_json())

# convert the object into a dict
inline_response200277_result_data_host_dict = inline_response200277_result_data_host_instance.to_dict()
# create an instance of InlineResponse200277ResultDataHost from a dict
inline_response200277_result_data_host_from_dict = InlineResponse200277ResultDataHost.from_dict(inline_response200277_result_data_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



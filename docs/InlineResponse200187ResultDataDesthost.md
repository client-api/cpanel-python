# InlineResponse200187ResultDataDesthost

The IP address or domain name that handles mail for the mailing list's domain. * A valid hostname. * An IPv4 address.  **Note:**    If the function **cannot** resolve the IP address to a hostname, it will return the IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200187_result_data_desthost import InlineResponse200187ResultDataDesthost

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200187ResultDataDesthost from a JSON string
inline_response200187_result_data_desthost_instance = InlineResponse200187ResultDataDesthost.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200187ResultDataDesthost.to_json())

# convert the object into a dict
inline_response200187_result_data_desthost_dict = inline_response200187_result_data_desthost_instance.to_dict()
# create an instance of InlineResponse200187ResultDataDesthost from a dict
inline_response200187_result_data_desthost_from_dict = InlineResponse200187ResultDataDesthost.from_dict(inline_response200187_result_data_desthost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



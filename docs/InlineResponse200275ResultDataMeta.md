# InlineResponse200275ResultDataMeta

An object containing metadata about the host's public key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The key&#39;s algorithm. | [optional] 
**body** | **str** | The host&#39;s public key. | [optional] 
**md5** | **str** | The key&#39;s [MD5](https://en.wikipedia.org/wiki/MD5) fingerprint. | [optional] 
**md5_printable** | **str** | A human-readable version of the key&#39;s MD5 fingerprint. | [optional] 
**sha256** | **str** | The key&#39;s [SHA-256](https://en.wikipedia.org/wiki/SHA-2) fingerprint. | [optional] 
**sha256_printable** | **str** | A human-readable version of the key&#39;s SHA-256 fingerprint. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200275_result_data_meta import InlineResponse200275ResultDataMeta

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200275ResultDataMeta from a JSON string
inline_response200275_result_data_meta_instance = InlineResponse200275ResultDataMeta.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200275ResultDataMeta.to_json())

# convert the object into a dict
inline_response200275_result_data_meta_dict = inline_response200275_result_data_meta_instance.to_dict()
# create an instance of InlineResponse200275ResultDataMeta from a dict
inline_response200275_result_data_meta_from_dict = InlineResponse200275ResultDataMeta.from_dict(inline_response200275_result_data_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



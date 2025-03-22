# InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_desc** | **str** | A description of the algorithm  that the DS key uses. | [optional] 
**algo_num** | **int** | A IETF-recognized DNSSEC Algorithm Number. | [optional] 
**digest** | **str** | The actual digest in the DS record. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20095_result_data_additional_properties_keys_additional_properties_digests import InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests from a JSON string
inline_response20095_result_data_additional_properties_keys_additional_properties_digests_instance = InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests.to_json())

# convert the object into a dict
inline_response20095_result_data_additional_properties_keys_additional_properties_digests_dict = inline_response20095_result_data_additional_properties_keys_additional_properties_digests_instance.to_dict()
# create an instance of InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests from a dict
inline_response20095_result_data_additional_properties_keys_additional_properties_digests_from_dict = InlineResponse20095ResultDataAdditionalPropertiesKeysAdditionalPropertiesDigests.from_dict(inline_response20095_result_data_additional_properties_keys_additional_properties_digests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20074ResultDataNoSslContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the address book. | [optional] 
**name** | **str** | The name of the address book. | [optional] 
**path** | **str** | The relative URL to the address book. | [optional] 
**url** | **str** | The absolute URL to the address book. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data_no_ssl_contacts import InlineResponse20074ResultDataNoSslContacts

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultDataNoSslContacts from a JSON string
inline_response20074_result_data_no_ssl_contacts_instance = InlineResponse20074ResultDataNoSslContacts.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultDataNoSslContacts.to_json())

# convert the object into a dict
inline_response20074_result_data_no_ssl_contacts_dict = inline_response20074_result_data_no_ssl_contacts_instance.to_dict()
# create an instance of InlineResponse20074ResultDataNoSslContacts from a dict
inline_response20074_result_data_no_ssl_contacts_from_dict = InlineResponse20074ResultDataNoSslContacts.from_dict(inline_response20074_result_data_no_ssl_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200569ResultDataOffers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **object** |  | [optional] 
**download** | **object** |  | [optional] 
**locale** | **object** |  | [optional] 
**mysql_version** | **object** |  | [optional] 
**new_bundled** | **object** |  | [optional] 
**packages** | [**InlineResponse200569ResultDataPackages**](InlineResponse200569ResultDataPackages.md) |  | [optional] 
**partial_version** | **object** |  | [optional] 
**php_version** | **object** |  | [optional] 
**response** | **object** |  | [optional] 
**version** | **object** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200569_result_data_offers import InlineResponse200569ResultDataOffers

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200569ResultDataOffers from a JSON string
inline_response200569_result_data_offers_instance = InlineResponse200569ResultDataOffers.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200569ResultDataOffers.to_json())

# convert the object into a dict
inline_response200569_result_data_offers_dict = inline_response200569_result_data_offers_instance.to_dict()
# create an instance of InlineResponse200569ResultDataOffers from a dict
inline_response200569_result_data_offers_from_dict = InlineResponse200569ResultDataOffers.from_dict(inline_response200569_result_data_offers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



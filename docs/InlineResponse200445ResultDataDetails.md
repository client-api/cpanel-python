# InlineResponse200445ResultDataDetails

An object contaning the CSR's contents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The CSR&#39;s Common Name or Distinguished Name. | [optional] 
**country_name** | **str** | The CSR&#39;s [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166) country code. | [optional] 
**created** | **int** | The CSR&#39;s creation date. | [optional] 
**domains** | **List[str]** | A list of the domains that the CSR covers. | [optional] 
**email_address** | **str** | The CSR&#39;s email address. | [optional] 
**friendly_name** | **str** | The CSR&#39;s friendly name. | [optional] 
**id** | **str** | The CSR&#39;s ID. | [optional] 
**key_algorithm** | **str** | The key algorithm that encrypts the CSR. | [optional] 
**locality_name** | **str** | The certificate&#39;s locality or city. | [optional] 
**modulus** | **str** | The CSR&#39;s modulus. | [optional] 
**organization_name** | **str** | The CSR&#39;s organization name. | [optional] 
**organizational_unit_name** | **str** | The CSR&#39;s organizational unit name. | [optional] 
**state_or_province_name** | **str** | The CSR&#39;s state or province name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200445_result_data_details import InlineResponse200445ResultDataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200445ResultDataDetails from a JSON string
inline_response200445_result_data_details_instance = InlineResponse200445ResultDataDetails.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200445ResultDataDetails.to_json())

# convert the object into a dict
inline_response200445_result_data_details_dict = inline_response200445_result_data_details_instance.to_dict()
# create an instance of InlineResponse200445ResultDataDetails from a dict
inline_response200445_result_data_details_from_dict = InlineResponse200445ResultDataDetails.from_dict(inline_response200445_result_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200305ResultDataDomainDetails

An object that contains information about the domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The Fully Qualified Domain Name (FQDN) that the function queries. | [optional] 
**status** | **str** | The status of the domain&#39;s certificate.  * &#x60;VALIDATED&#x60; - The domain has been validated. * &#x60;NOTVALIDATED&#x60; - The domain has **not** been validated. * &#x60;AWAITINGBRAND&#x60; - The domain has **not** been validated, and is awaiting brand approval. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200305_result_data_domain_details import InlineResponse200305ResultDataDomainDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200305ResultDataDomainDetails from a JSON string
inline_response200305_result_data_domain_details_instance = InlineResponse200305ResultDataDomainDetails.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200305ResultDataDomainDetails.to_json())

# convert the object into a dict
inline_response200305_result_data_domain_details_dict = inline_response200305_result_data_domain_details_instance.to_dict()
# create an instance of InlineResponse200305ResultDataDomainDetails from a dict
inline_response200305_result_data_domain_details_from_dict = InlineResponse200305ResultDataDomainDetails.from_dict(inline_response200305_result_data_domain_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



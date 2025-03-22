# InlineResponse200444ResultDataDetailsSubject

An object containing the certificate's ownership details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The certificate&#39;s Common Name or Distinguished Name. | [optional] 
**country_name** | **str** | The certificate&#39;s two-letter country code. | [optional] 
**email_address** | **str** | The certificate&#39;s email address. | [optional] 
**locality_name** | **str** | The certificate&#39;s locality or city. | [optional] 
**organization_name** | **str** | The certificate&#39;s organization name. | [optional] 
**state_or_province_name** | **str** | The certificate&#39;s state or province name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200444_result_data_details_subject import InlineResponse200444ResultDataDetailsSubject

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200444ResultDataDetailsSubject from a JSON string
inline_response200444_result_data_details_subject_instance = InlineResponse200444ResultDataDetailsSubject.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200444ResultDataDetailsSubject.to_json())

# convert the object into a dict
inline_response200444_result_data_details_subject_dict = inline_response200444_result_data_details_subject_instance.to_dict()
# create an instance of InlineResponse200444ResultDataDetailsSubject from a dict
inline_response200444_result_data_details_subject_from_dict = InlineResponse200444ResultDataDetailsSubject.from_dict(inline_response200444_result_data_details_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



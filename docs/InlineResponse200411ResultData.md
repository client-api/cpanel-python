# InlineResponse200411ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cab** | **str** | The CA bundle&#39;s contents (if applicable). | [optional] 
**crt** | **str** | The certificate&#39;s contents. | [optional] 
**crt_origin** | **str** | The username that generated the certificate. | [optional] 
**domain** | **str** | The domain that generated the private key. | [optional] 
**ip** | **str** | The IP address. | [optional] 
**key** | **str** | The private key. | [optional] 
**key_origin** | **str** | The username that generated the private key. | [optional] 
**searched_users** | **List[str]** | The cPanel accounts that the system searched for domain information. | [optional] 
**status** | **int** | Whether the certificate is active. * &#x60;1&#x60; - Active. * &#x60;0&#x60; - Inactive. | [optional] 
**statusmsg** | **str** | The certificate&#39;s status. | [optional] 
**user** | **str** | The username that stores the private key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200411_result_data import InlineResponse200411ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200411ResultData from a JSON string
inline_response200411_result_data_instance = InlineResponse200411ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200411ResultData.to_json())

# convert the object into a dict
inline_response200411_result_data_dict = inline_response200411_result_data_instance.to_dict()
# create an instance of InlineResponse200411ResultData from a dict
inline_response200411_result_data_from_dict = InlineResponse200411ResultData.from_dict(inline_response200411_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



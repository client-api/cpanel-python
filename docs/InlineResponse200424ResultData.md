# InlineResponse200424ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that the function used to install the certificate. | [optional] 
**cert_id** | **str** | The certificate ID. | [optional] 
**domain** | **str** | The domain that the certificate covers. | [optional] 
**extra_certificate_domains** | **List[str]** | The domains that require extra certificates for mail and other services. | [optional] 
**html** | **str** | The results, in HTML format. | [optional] 
**ip** | [**InlineResponse200424ResultDataIp**](InlineResponse200424ResultDataIp.md) |  | [optional] 
**key_id** | **str** | The key ID. | [optional] 
**message** | **str** | The results, in text format. | [optional] 
**statusmsg** | **str** | The results. | [optional] 
**user** | **str** | The domain&#39;s owner. | [optional] 
**warning_domains** | **List[str]** | The domains that the certificate does not cover. | [optional] 
**working_domains** | **List[str]** | The domains that the certificate covers. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200424_result_data import InlineResponse200424ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200424ResultData from a JSON string
inline_response200424_result_data_instance = InlineResponse200424ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200424ResultData.to_json())

# convert the object into a dict
inline_response200424_result_data_dict = inline_response200424_result_data_instance.to_dict()
# create an instance of InlineResponse200424ResultData from a dict
inline_response200424_result_data_from_dict = InlineResponse200424ResultData.from_dict(inline_response200424_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



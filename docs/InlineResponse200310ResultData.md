# InlineResponse200310ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_pem** | **str** | The certificate&#39;s text. * &#x60;null&#x60; - The certificate is not available. * A certificate file in [Base64 PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format. | [optional] 
**encrypted_action_urls** | [**InlineResponse200310ResultDataEncryptedActionUrls**](InlineResponse200310ResultDataEncryptedActionUrls.md) |  | [optional] 
**status_code** | **str** | The status code of the certificate. | [optional] 
**status_message** | **str** | An error message from the certificate provider. For example, why a certificate authority rejected an SSL certificate.  **Note:**  If no error message exists, this will return an empty string. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200310_result_data import InlineResponse200310ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200310ResultData from a JSON string
inline_response200310_result_data_instance = InlineResponse200310ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200310ResultData.to_json())

# convert the object into a dict
inline_response200310_result_data_dict = inline_response200310_result_data_instance.to_dict()
# create an instance of InlineResponse200310ResultData from a dict
inline_response200310_result_data_from_dict = InlineResponse200310ResultData.from_dict(inline_response200310_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



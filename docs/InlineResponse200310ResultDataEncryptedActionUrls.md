# InlineResponse200310ResultDataEncryptedActionUrls

An object that contains encrypted URLs a user must click to complete their SSL certificate order.  **Note:**  This return may also contain additional key values. For more information, read [Sectigo's documentation](https://sectigo.com/uploads/files/CollectSSL-v1.17.pdf).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ev_click_through_status** | **str** | A URL the user must click to electronically sign an agreement for their Extended Validation (EV) certificate. * An encrypted URL. * &#x60;null&#x60; - No action required. | [optional] 
**ov_callback_status** | **str** | URL the user must click to verify their identity by phone to complete their Organization Validation (OV) certificate order. * An encrypted URL. * &#x60;null&#x60; - No action required. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200310_result_data_encrypted_action_urls import InlineResponse200310ResultDataEncryptedActionUrls

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200310ResultDataEncryptedActionUrls from a JSON string
inline_response200310_result_data_encrypted_action_urls_instance = InlineResponse200310ResultDataEncryptedActionUrls.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200310ResultDataEncryptedActionUrls.to_json())

# convert the object into a dict
inline_response200310_result_data_encrypted_action_urls_dict = inline_response200310_result_data_encrypted_action_urls_instance.to_dict()
# create an instance of InlineResponse200310ResultDataEncryptedActionUrls from a dict
inline_response200310_result_data_encrypted_action_urls_from_dict = InlineResponse200310ResultDataEncryptedActionUrls.from_dict(inline_response200310_result_data_encrypted_action_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



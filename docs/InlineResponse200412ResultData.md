# InlineResponse200412ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cabundle** | **str** | The CA bundle&#39;s contents (if applicable). | [optional] 
**certificate** | **str** | The certificate&#39;s contents. | [optional] 
**is_self_signed** | **int** | Whether the certificate is self-signed. * &#x60;1&#x60; - Self-signed. * &#x60;0&#x60; - **Not** self-signed. | [optional] 
**key** | **str** | The private key. | [optional] 
**subject_common_name_ip** | **str** | The IP address. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200412_result_data import InlineResponse200412ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200412ResultData from a JSON string
inline_response200412_result_data_instance = InlineResponse200412ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200412ResultData.to_json())

# convert the object into a dict
inline_response200412_result_data_dict = inline_response200412_result_data_instance.to_dict()
# create an instance of InlineResponse200412ResultData from a dict
inline_response200412_result_data_from_dict = InlineResponse200412ResultData.from_dict(inline_response200412_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



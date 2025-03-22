# InlineResponse200488ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | The domain&#39;s bandwidth usage, in bytes. | [optional] 
**domain** | **str** | The domain for which to display bandwidth statistics.  **Note:**  The function only returns this value if the &#x60;protocol&#x60; return&#39;s value is &#x60;http&#x60;. | [optional] 
**month_start** | **int** | The beginning of the report window. | [optional] 
**protocol** | **str** | The protocol for which to provide data.   * &#x60;http&#x60;   * &#x60;imap&#x60;   * &#x60;smtp&#x60;   * &#x60;pop3&#x60;   * &#x60;ftp&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200488_result_data import InlineResponse200488ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200488ResultData from a JSON string
inline_response200488_result_data_instance = InlineResponse200488ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200488ResultData.to_json())

# convert the object into a dict
inline_response200488_result_data_dict = inline_response200488_result_data_instance.to_dict()
# create an instance of InlineResponse200488ResultData from a dict
inline_response200488_result_data_from_dict = InlineResponse200488ResultData.from_dict(inline_response200488_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



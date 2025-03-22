# InlineResponse200220ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The DKIM private key&#39;s associated domain. | [optional] 
**msg** | **str** | The DKIM private key&#39;s installation status message. | [optional] 
**status** | **int** | Whether the system installed the DKIM private key to the local server. * &#x60;1&#x60; - The system installed the DKIM private key. * &#x60;0&#x60; - The system **cannot** install the DKIM private key. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200220_result_data import InlineResponse200220ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200220ResultData from a JSON string
inline_response200220_result_data_instance = InlineResponse200220ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200220ResultData.to_json())

# convert the object into a dict
inline_response200220_result_data_dict = inline_response200220_result_data_instance.to_dict()
# create an instance of InlineResponse200220ResultData from a dict
inline_response200220_result_data_from_dict = InlineResponse200220ResultData.from_dict(inline_response200220_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20082ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The queried domain. | [optional] 
**error** | **str** | An error message that details the reason why the local server&#39;s authoritative check failed.  **Note:**  The function **only** returns this value when the check fails. | [optional] 
**local_authority** | **int** | Whether the local server is authoritative for the domain&#39;s DNS records.  * &#x60;1&#x60; — The local server is authoritative for the domain&#39;s DNS records. * &#x60;0&#x60; — The local server is **not** authoritative for the domain&#39;s DNS records. | [optional] 
**nameservers** | **List[str]** | The domain&#39;s nameservers, if any exist. | [optional] 
**zone** | **str** | The domain&#39;s DNS zone, if one exists.  * &#x60;null&#x60; — No valid DNS zone. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20082_result_data import InlineResponse20082ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20082ResultData from a JSON string
inline_response20082_result_data_instance = InlineResponse20082ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20082ResultData.to_json())

# convert the object into a dict
inline_response20082_result_data_dict = inline_response20082_result_data_instance.to_dict()
# create an instance of InlineResponse20082ResultData from a dict
inline_response20082_result_data_from_dict = InlineResponse20082ResultData.from_dict(inline_response20082_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



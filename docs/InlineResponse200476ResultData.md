# InlineResponse200476ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of the cPanel user&#39;s domain. | [optional] 
**metadata** | [**InlineResponse200476ResultMetadata**](InlineResponse200476ResultMetadata.md) |  | [optional] 
**quota** | [**InlineResponse200476ResultQuota**](InlineResponse200476ResultQuota.md) |  | [optional] 
**redirection_enabled** | **int** | Whether the domain redirects to another URL. * 1 - Redirects. * 0 - Doesn&#39;t redirect. | [optional] 
**shared_doc_root** | **int** | whether the sitejet domain is sharing the document_root. * 1 - document_root is shared. * 0 - document_root is not shared. | [optional] 
**is_restore_point_available** | **int** | Whether the sitejet domain has a restore point. * &#x60;1&#x60; – Restore point is available. * &#x60;0&#x60; – Restore point is not available. | [optional] 
**status** | [**InlineResponse200476ResultStatus**](InlineResponse200476ResultStatus.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200476_result_data import InlineResponse200476ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200476ResultData from a JSON string
inline_response200476_result_data_instance = InlineResponse200476ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200476ResultData.to_json())

# convert the object into a dict
inline_response200476_result_data_dict = inline_response200476_result_data_instance.to_dict()
# create an instance of InlineResponse200476ResultData from a dict
inline_response200476_result_data_from_dict = InlineResponse200476ResultData.from_dict(inline_response200476_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200305ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_urls** | [**InlineResponse200305ResultDataActionUrls**](InlineResponse200305ResultDataActionUrls.md) |  | [optional] 
**domain_details** | [**InlineResponse200305ResultDataDomainDetails**](InlineResponse200305ResultDataDomainDetails.md) |  | [optional] 
**status_details** | [**InlineResponse200305ResultDataStatusDetails**](InlineResponse200305ResultDataStatusDetails.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200305_result_data import InlineResponse200305ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200305ResultData from a JSON string
inline_response200305_result_data_instance = InlineResponse200305ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200305ResultData.to_json())

# convert the object into a dict
inline_response200305_result_data_dict = inline_response200305_result_data_instance.to_dict()
# create an instance of InlineResponse200305ResultData from a dict
inline_response200305_result_data_from_dict = InlineResponse200305ResultData.from_dict(inline_response200305_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



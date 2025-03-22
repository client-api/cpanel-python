# InlineResponse200111ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_domains** | **List[str]** | An array of string values that lists the addon domains on the cPanel account. | [optional] 
**main_domain** | **List[str]** | The cPanel account&#39;s main domain. | [optional] 
**parked_domains** | **List[str]** | An array of string values that lists the parked domains on the cPanel account. | [optional] 
**sub_domains** | **List[str]** | An array of string values that lists the subdomains on the cPanel account. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200111_result_data import InlineResponse200111ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200111ResultData from a JSON string
inline_response200111_result_data_instance = InlineResponse200111ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200111ResultData.to_json())

# convert the object into a dict
inline_response200111_result_data_dict = inline_response200111_result_data_instance.to_dict()
# create an instance of InlineResponse200111ResultData from a dict
inline_response200111_result_data_from_dict = InlineResponse200111ResultData.from_dict(inline_response200111_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



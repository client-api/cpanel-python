# InlineResponse200583ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | **List[str]** | An array of domains that your changes will affect. | [optional] 
**domain** | **str** | The domain. | [optional] 
**enabled** | **int** | Whether Greylisting is enabled. * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — Disabled. | [optional] 
**searchhint** | **str** | A comma-separated list of domain-related search terms. | [optional] 
**type** | **str** | The domain type. * &#x60;main&#x60; — A main domain. * &#x60;sub&#x60; — A subdomain. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200583_result_data import InlineResponse200583ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200583ResultData from a JSON string
inline_response200583_result_data_instance = InlineResponse200583ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200583ResultData.to_json())

# convert the object into a dict
inline_response200583_result_data_dict = inline_response200583_result_data_instance.to_dict()
# create an instance of InlineResponse200583ResultData from a dict
inline_response200583_result_data_from_dict = InlineResponse200583ResultData.from_dict(inline_response200583_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



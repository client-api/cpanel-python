# InlineResponse200569ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[InlineResponse200569ResultDataOffers]**](InlineResponse200569ResultDataOffers.md) | This array contains the returned value from [wordpress.org&#39;s](https://wordpress.org/) Version Check API.  **Note:**   For additional information about the returned values, read [WordPress&#39;s Version Check API](https://codex.wordpress.org/WordPress.org_API) documentation. | [optional] 
**translations** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200569_result_data import InlineResponse200569ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200569ResultData from a JSON string
inline_response200569_result_data_instance = InlineResponse200569ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200569ResultData.to_json())

# convert the object into a dict
inline_response200569_result_data_dict = inline_response200569_result_data_instance.to_dict()
# create an instance of InlineResponse200569ResultData from a dict
inline_response200569_result_data_from_dict = InlineResponse200569ResultData.from_dict(inline_response200569_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200518ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | The API token&#39;s creation date and time. | [optional] 
**expires_at** | **int** | The API token&#39;s expiration time.  * null — The API token does **not** expire. | [optional] 
**features** | **List[str]** | The account features that the API token has access to.  * An empty array — The API token has full access. | [optional] 
**has_full_access** | **int** | Whether the API token has full access to the account&#39;s features.  * &#x60;1&#x60; — The API token has full access to the account&#39;s features. * &#x60;0&#x60; — The API token does **not** have full access to the account&#39;s features. | [optional] 
**name** | **str** | The API token&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200518_result_data import InlineResponse200518ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200518ResultData from a JSON string
inline_response200518_result_data_instance = InlineResponse200518ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200518ResultData.to_json())

# convert the object into a dict
inline_response200518_result_data_dict = inline_response200518_result_data_instance.to_dict()
# create an instance of InlineResponse200518ResultData from a dict
inline_response200518_result_data_from_dict = InlineResponse200518ResultData.from_dict(inline_response200518_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



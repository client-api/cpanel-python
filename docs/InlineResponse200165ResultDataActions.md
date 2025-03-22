# InlineResponse200165ResultDataActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The filter&#39;s action. * &#x60;deliver&#x60; -  The filter sends mail to the destination address. * &#x60;fail&#x60; -  The filter forces a delivery failure. * &#x60;finish&#x60; -  The filter stops message processing. * &#x60;save&#x60; -  The filter saves mail to the destination file. * &#x60;pipe&#x60; -  The filter sends mail to the destination application. | [optional] 
**dest** | [**InlineResponse200165ResultDataActionsDest**](InlineResponse200165ResultDataActionsDest.md) |  | [optional] 
**number** | **int** | The filter&#39;s position in the order of the account&#39;s filters. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200165_result_data_actions import InlineResponse200165ResultDataActions

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200165ResultDataActions from a JSON string
inline_response200165_result_data_actions_instance = InlineResponse200165ResultDataActions.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200165ResultDataActions.to_json())

# convert the object into a dict
inline_response200165_result_data_actions_dict = inline_response200165_result_data_actions_instance.to_dict()
# create an instance of InlineResponse200165ResultDataActions from a dict
inline_response200165_result_data_actions_from_dict = InlineResponse200165ResultDataActions.from_dict(inline_response200165_result_data_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



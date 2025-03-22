# InlineResponse20071ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the cPanel account can contact their hosting provider from the cPanel interface.  * &#x60;1&#x60; — The cPanel account can contact their hosting provider from the cPanel interface. * &#x60;0&#x60; — The cPanel account **cannot** contact their hosting provider from the cPanel interface. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20071_result_data import InlineResponse20071ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20071ResultData from a JSON string
inline_response20071_result_data_instance = InlineResponse20071ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20071ResultData.to_json())

# convert the object into a dict
inline_response20071_result_data_dict = inline_response20071_result_data_instance.to_dict()
# create an instance of InlineResponse20071ResultData from a dict
inline_response20071_result_data_from_dict = InlineResponse20071ResultData.from_dict(inline_response20071_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20057ResultDataResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address or forwarder. | [optional] 
**fwd** | **str** | The destination of the forwarder (if applicable). | [optional] 
**reason** | **str** | The explanation of the outcome for each operation. | [optional] 
**status** | **int** | The outcome of each operation.  * &#x60;1&#x60; — Success. * &#x60;0&#x60; — Failed. | [optional] 
**type** | **str** | The type of email address.  * &#x60;email&#x60; — A regular email account. * &#x60;fwd&#x60; — A forwarder. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20057_result_data_results import InlineResponse20057ResultDataResults

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20057ResultDataResults from a JSON string
inline_response20057_result_data_results_instance = InlineResponse20057ResultDataResults.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20057ResultDataResults.to_json())

# convert the object into a dict
inline_response20057_result_data_results_dict = inline_response20057_result_data_results_instance.to_dict()
# create an instance of InlineResponse20057ResultDataResults from a dict
inline_response20057_result_data_results_from_dict = InlineResponse20057ResultDataResults.from_dict(inline_response20057_result_data_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



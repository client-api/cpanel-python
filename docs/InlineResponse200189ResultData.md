# InlineResponse200189ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysaccept** | **int** | Whether the domain&#39;s highest-priority mail exchanger accepts local mail. * &#x60;1&#x60; - Accept local mail. * &#x60;0&#x60; - Does **not** accept local mail. | [optional] 
**detected** | **str** | The domain&#39;s highest-priority mail exchanger&#39;s type. * &#x60;auto&#x60; * &#x60;local&#x60; * &#x60;remote&#x60; * &#x60;secondary&#x60; | [optional] 
**domain** | **str** | The domain name. | [optional] 
**entries** | [**List[InlineResponse200189ResultEntries]**](InlineResponse200189ResultEntries.md) | An array of objects that contains information about mail exchangers. | [optional] 
**local** | **int** | Whether the domain&#39;s highest priority mail exchanger is a local mail exchanger. * &#x60;1&#x60; - Local. * &#x60;0&#x60; - **Not** local. | [optional] 
**mx** | **str** | The domain&#39;s highest-priority mail exchanger&#39;s name. | [optional] 
**mxcheck** | **str** | The domain&#39;s highest-priority mail exchanger&#39;s type. * &#x60;auto&#x60; * &#x60;local&#x60; * &#x60;remote&#x60; * &#x60;secondary&#x60; | [optional] 
**remote** | **int** | Whether the domain&#39;s highest-priority mail exchanger is remote. * &#x60;1&#x60; - Remote. * &#x60;0&#x60; - **Not** remote. | [optional] 
**secondary** | **int** | Whether the domain&#39;s highest-priority mail exchanger is secondary. * &#x60;1&#x60; - Secondary. * &#x60;0&#x60; - **Not** secondary. | [optional] 
**status** | **int** | Whether the function succeeded. * &#x60;1&#x60; - Success. * &#x60;0&#x60; - Failure. | [optional] 
**statusmsg** | **str** | A success or error message message. * A success message. * An error message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200189_result_data import InlineResponse200189ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200189ResultData from a JSON string
inline_response200189_result_data_instance = InlineResponse200189ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200189ResultData.to_json())

# convert the object into a dict
inline_response200189_result_data_dict = inline_response200189_result_data_instance.to_dict()
# create an instance of InlineResponse200189ResultData from a dict
inline_response200189_result_data_from_dict = InlineResponse200189ResultData.from_dict(inline_response200189_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200142ResultDataCheckmx

An object containing the mail exchanger's data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **int** | Whether a change occurred during the function. * &#x60;1&#x60; - Change occurred. * &#x60;0&#x60; - **No** change. | [optional] 
**detected** | **str** | The mail exchanger type. * &#x60;auto&#x60; * &#x60;local&#x60; * &#x60;secondary&#x60; * &#x60;remote&#x60; | [optional] 
**isprimary** | **int** | Whether the mail exchanger is the primary mail exchanger. * &#x60;1&#x60; - Primary. * &#x60;0&#x60; - **Not** primary. | [optional] 
**issecondary** | **int** | Whether the mail exchanger is a secondary exchanger. * &#x60;1&#x60; - Secondary. * &#x60;0&#x60; - **Not** secondary. | [optional] 
**local** | **int** | Whether the mail exchanger is a local exchanger. * &#x60;1&#x60; - Local. * &#x60;0&#x60; - **Not** local. | [optional] 
**mxcheck** | **str** | The mail exchanger type. * &#x60;auto&#x60; * &#x60;local&#x60; * &#x60;secondary&#x60; * &#x60;remote&#x60; | [optional] 
**remote** | **int** | Whether the mail exchanger is a remote exchanger. * &#x60;1&#x60; - Remote. * &#x60;0&#x60; - **Not** remote. | [optional] 
**secondary** | **int** | Whether the mail exchanger is a secondary exchanger. * &#x60;1&#x60; - Secondary. * &#x60;0&#x60; - **Not** secondary. | [optional] 
**warnings** | **List[str]** | Warning messages, if any exist. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200142_result_data_checkmx import InlineResponse200142ResultDataCheckmx

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200142ResultDataCheckmx from a JSON string
inline_response200142_result_data_checkmx_instance = InlineResponse200142ResultDataCheckmx.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200142ResultDataCheckmx.to_json())

# convert the object into a dict
inline_response200142_result_data_checkmx_dict = inline_response200142_result_data_checkmx_instance.to_dict()
# create an instance of InlineResponse200142ResultDataCheckmx from a dict
inline_response200142_result_data_checkmx_from_dict = InlineResponse200142ResultDataCheckmx.from_dict(inline_response200142_result_data_checkmx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



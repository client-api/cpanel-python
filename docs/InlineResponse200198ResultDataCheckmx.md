# InlineResponse200198ResultDataCheckmx

An object containing the mail exchanger's data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **int** | Whether a change occurred during the function. * &#x60;1&#x60; — Change occurred. * &#x60;0&#x60; — **No** change. | [optional] 
**detected** | **str** | The mail exchanger type. * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role. * &#x60;local&#x60; — Always accept the domain&#39;s mail. * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available. * &#x60;remote&#x60; — Do **not** accept mail. | [optional] 
**isprimary** | **int** | Whether the mail exchanger is the primary mail exchanger. * &#x60;1&#x60; —  Primary. * &#x60;0&#x60; — **Not** primary. | [optional] 
**issecondary** | **int** | Whether the mail exchanger is a secondary exchanger. * &#x60;1&#x60; — Secondary. * &#x60;0&#x60; — **Not** secondary. | [optional] 
**local** | **int** | Whether the mail exchanger is a local exchanger. * &#x60;1&#x60; — Local. * &#x60;0&#x60; — **Not** local. | [optional] 
**mxcheck** | **str** | The mail exchanger type.   * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role.   * &#x60;local&#x60; — Always accept the domain&#39;s mail.   * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available.   * &#x60;remote&#x60; — Do **not** accept mail. | [optional] 
**remote** | **int** | Whether the mail exchanger is a remote exchanger. * &#x60;1&#x60; — Remote. * &#x60;0&#x60; — **Not** remote. | [optional] 
**secondary** | **int** | Whether the mail exchanger is a secondary exchanger. * &#x60;1&#x60; — Secondary. * &#x60;0&#x60; — **Not** secondary. | [optional] 
**warnings** | **List[str]** | An array of warning messages, if any exist. One or more warning messages. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200198_result_data_checkmx import InlineResponse200198ResultDataCheckmx

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200198ResultDataCheckmx from a JSON string
inline_response200198_result_data_checkmx_instance = InlineResponse200198ResultDataCheckmx.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200198ResultDataCheckmx.to_json())

# convert the object into a dict
inline_response200198_result_data_checkmx_dict = inline_response200198_result_data_checkmx_instance.to_dict()
# create an instance of InlineResponse200198ResultDataCheckmx from a dict
inline_response200198_result_data_checkmx_from_dict = InlineResponse200198ResultDataCheckmx.from_dict(inline_response200198_result_data_checkmx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



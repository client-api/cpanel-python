# InlineResponse200198ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkmx** | [**InlineResponse200198ResultDataCheckmx**](InlineResponse200198ResultDataCheckmx.md) |  | [optional] 
**detected** | **str** | The mail exchanger type.   * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role.   * &#x60;local&#x60; — Always accept the domain&#39;s mail.   * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available.   * &#x60;remote&#x60; — Do **not** accept mail. | [optional] 
**local** | **int** | Whether the mail exchanger is a local exchanger. * &#x60;1&#x60; — Local. * &#x60;0&#x60; — **Not** local. | [optional] 
**mxcheck** | **str** | The mail exchanger type.   * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role.   * &#x60;local&#x60; — Always accept the domain&#39;s mail.   * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available.   * &#x60;remote&#x60; — Do **not** accept mail. | [optional] 
**remote** | **int** | Whether the mail exchanger is a remote exchanger. * &#x60;1&#x60; — Remote. * &#x60;0&#x60; — **Not** remote. | [optional] 
**results** | **str** | A message of success or a reason for failure. * A message of success that includes the new type. * A string that describes an error. | [optional] 
**secondary** | **int** | Whether the mail exchanger is a secondary exchanger. * &#x60;1&#x60; — Secondary. * &#x60;0&#x60; — **Not** secondary. | [optional] 
**status** | **int** | Whether the function succeeded. * &#x60;1&#x60; — Success. * &#x60;0&#x60; — Failure. | [optional] 
**statusmsg** | **str** | A message of success or a reason for failure. * A message of success that includes the new type. * A string that describes an error. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200198_result_data import InlineResponse200198ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200198ResultData from a JSON string
inline_response200198_result_data_instance = InlineResponse200198ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200198ResultData.to_json())

# convert the object into a dict
inline_response200198_result_data_dict = inline_response200198_result_data_instance.to_dict()
# create an instance of InlineResponse200198ResultData from a dict
inline_response200198_result_data_from_dict = InlineResponse200198ResultData.from_dict(inline_response200198_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



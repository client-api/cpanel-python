# InlineResponse200164ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskused** | **float** | The disk space that the email account uses. * A positive floating-point value that represents the disk space, used in megabytes (MB). * &#x60;0&#x60; - The account posesses an unlimited disk quota. | [optional] 
**domain** | **str** | The email account&#39;s domain. | [optional] 
**login** | **str** | The email address or the main account username. | [optional] 
**user** | **str** | The email account&#39;s username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200164_result_data import InlineResponse200164ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200164ResultData from a JSON string
inline_response200164_result_data_instance = InlineResponse200164ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200164ResultData.to_json())

# convert the object into a dict
inline_response200164_result_data_dict = inline_response200164_result_data_instance.to_dict()
# create an instance of InlineResponse200164ResultData from a dict
inline_response200164_result_data_from_dict = InlineResponse200164ResultData.from_dict(inline_response200164_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



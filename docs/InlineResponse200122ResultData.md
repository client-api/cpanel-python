# InlineResponse200122ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain. A valid domain on the account. | [optional] 
**email** | **str** | The email address. An email address on the account. | [optional] 
**forward** | **str** | The method that the system will use to handle the address&#39;s mail. - An email address  The system forwards mail to this address. - :fail:  The system bounces mail back to the sender and sends a failure message. - :blackhole:  The system deletes mail without a failure message. - The path to an application  The system pipes mail to this application. - A username  The system forwards mail to this system account. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200122_result_data import InlineResponse200122ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200122ResultData from a JSON string
inline_response200122_result_data_instance = InlineResponse200122ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200122ResultData.to_json())

# convert the object into a dict
inline_response200122_result_data_dict = inline_response200122_result_data_instance.to_dict()
# create an instance of InlineResponse200122ResultData from a dict
inline_response200122_result_data_from_dict = InlineResponse200122ResultData.from_dict(inline_response200122_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



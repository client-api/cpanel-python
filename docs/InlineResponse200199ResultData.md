# InlineResponse200199ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest** | **str** | The destination to which the system sends unroutable mail. - An email address  The system forwards mail to this address. - :fail:  The system bounces mail back to the sender, and sends a failure message. - :blackhole:  The system deletes mail without a failure message. - The path to an application  The system pipes mail to this application. | [optional] 
**domain** | **str** | The domain. A valid domain on the account. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200199_result_data import InlineResponse200199ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200199ResultData from a JSON string
inline_response200199_result_data_instance = InlineResponse200199ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200199ResultData.to_json())

# convert the object into a dict
inline_response200199_result_data_dict = inline_response200199_result_data_instance.to_dict()
# create an instance of InlineResponse200199ResultData from a dict
inline_response200199_result_data_from_dict = InlineResponse200199ResultData.from_dict(inline_response200199_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



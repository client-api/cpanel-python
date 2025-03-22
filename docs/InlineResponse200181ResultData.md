# InlineResponse200181ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultaddress** | **str** | The domain&#39;s default address. * An email account username - The system forwards unroutable mail to this address. * &#x60;:fail:&#x60; - The system bounces unroutable mail back to the sender, and sends a failure message. * &#x60;:blackhole:&#x60; - The system deletes unroutable mail without a failure message. * The path to an application - The system pipes unroutable mail to this application. | [optional] 
**domain** | **str** | The domain name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200181_result_data import InlineResponse200181ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200181ResultData from a JSON string
inline_response200181_result_data_instance = InlineResponse200181ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200181ResultData.to_json())

# convert the object into a dict
inline_response200181_result_data_dict = inline_response200181_result_data_instance.to_dict()
# create an instance of InlineResponse200181ResultData from a dict
inline_response200181_result_data_from_dict = InlineResponse200181ResultData.from_dict(inline_response200181_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



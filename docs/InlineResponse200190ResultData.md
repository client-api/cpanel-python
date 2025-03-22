# InlineResponse200190ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**InlineResponse200190ResultDataEmail**](InlineResponse200190ResultDataEmail.md) |  | [optional] 
**login** | [**InlineResponse200190ResultDataLogin**](InlineResponse200190ResultDataLogin.md) |  | [optional] 
**suspended_incoming** | **int** | Whether incoming email for the email account is suspended. * &#x60;1&#x60; - Suspended. * &#x60;0&#x60; - Not suspended. | [optional] 
**suspended_login** | **int** | Whether logins for the email account are suspended. * &#x60;1&#x60; - Suspended. * &#x60;0&#x60; - Not suspended. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200190_result_data import InlineResponse200190ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200190ResultData from a JSON string
inline_response200190_result_data_instance = InlineResponse200190ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200190ResultData.to_json())

# convert the object into a dict
inline_response200190_result_data_dict = inline_response200190_result_data_instance.to_dict()
# create an instance of InlineResponse200190ResultData from a dict
inline_response200190_result_data_from_dict = InlineResponse200190ResultData.from_dict(inline_response200190_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



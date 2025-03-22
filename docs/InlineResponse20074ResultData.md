# InlineResponse20074ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activesync** | [**InlineResponse20074ResultDataActivesync**](InlineResponse20074ResultDataActivesync.md) |  | [optional] 
**no_ssl** | [**InlineResponse20074ResultDataNoSsl**](InlineResponse20074ResultDataNoSsl.md) |  | [optional] 
**ssl** | [**InlineResponse20074ResultDataSsl**](InlineResponse20074ResultDataSsl.md) |  | [optional] 
**user** | **str** | The cPanel user or email account user to whom the returned connection information pertains.  If you do **not** specify the &#x60;user&#x60; parameter, this function returns the authenticated cPanel user. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20074_result_data import InlineResponse20074ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20074ResultData from a JSON string
inline_response20074_result_data_instance = InlineResponse20074ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20074ResultData.to_json())

# convert the object into a dict
inline_response20074_result_data_dict = inline_response20074_result_data_instance.to_dict()
# create an instance of InlineResponse20074ResultData from a dict
inline_response20074_result_data_from_dict = InlineResponse20074ResultData.from_dict(inline_response20074_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



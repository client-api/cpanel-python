# InlineResponse200248ResultDataSupports

This object contains the features that the FTP daemon supports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_without_domain** | **int** | Whether the FTP daemon supports username authentication without the user&#39;s domain.  * &#x60;1&#x60; – Supported. * &#x60;0&#x60; – **Not** supported. | [optional] 
**quota** | **int** | Whether the FTP daemon supports disk quotas.  * &#x60;1&#x60; – Supported. * &#x60;0&#x60; – **Not** supported. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200248_result_data_supports import InlineResponse200248ResultDataSupports

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200248ResultDataSupports from a JSON string
inline_response200248_result_data_supports_instance = InlineResponse200248ResultDataSupports.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200248ResultDataSupports.to_json())

# convert the object into a dict
inline_response200248_result_data_supports_dict = inline_response200248_result_data_supports_instance.to_dict()
# create an instance of InlineResponse200248ResultDataSupports from a dict
inline_response200248_result_data_supports_from_dict = InlineResponse200248ResultDataSupports.from_dict(inline_response200248_result_data_supports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



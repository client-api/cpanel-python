# InlineResponse200554ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | A valid domain name on the virtual host. | [optional] 
**is_proxy** | **int** | Whether the system automatically created the service subdomain or a user manually created the domain. * &#x60;1&#x60; - The system automatically created the service subdomain. * &#x60;0&#x60; - A user manually created the domain.  **Note:**  If a user manually creates a subdomain that matches a preassigned subdomain (for example, cpanel or whm), then the function returns &#x60;0&#x60;. | [optional] 
**vhost_name** | **str** | The name of the virtual host or website. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200554_result_data import InlineResponse200554ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200554ResultData from a JSON string
inline_response200554_result_data_instance = InlineResponse200554ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200554ResultData.to_json())

# convert the object into a dict
inline_response200554_result_data_dict = inline_response200554_result_data_instance.to_dict()
# create an instance of InlineResponse200554ResultData from a dict
inline_response200554_result_data_from_dict = InlineResponse200554ResultData.from_dict(inline_response200554_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



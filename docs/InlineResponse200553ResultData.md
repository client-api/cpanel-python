# InlineResponse200553ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain name. | [optional] 
**proxy_subdomains** | **List[str]** | An array of service subdomains (proxy subdomains) listed for the domain.  **Note:**  This only returns values when &#x60;vhost_is_ssl&#x60; equals &#x60;1&#x60;. | [optional] 
**vhost_is_ssl** | **int** | Whether an SSL certificate secures the domain. * &#x60;1&#x60; - Secured. * &#x60;0&#x60; - **Not** secured. | [optional] 
**vhost_name** | **str** | The name of the virtual host. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200553_result_data import InlineResponse200553ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200553ResultData from a JSON string
inline_response200553_result_data_instance = InlineResponse200553ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200553ResultData.to_json())

# convert the object into a dict
inline_response200553_result_data_dict = inline_response200553_result_data_instance.to_dict()
# create an instance of InlineResponse200553ResultData from a dict
inline_response200553_result_data_from_dict = InlineResponse200553ResultData.from_dict(inline_response200553_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



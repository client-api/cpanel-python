# InlineResponse20065ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The type of path * &#x60;home&#x60; — The cPanel account&#39;s entire home directory. * &#x60;mail&#x60; — The cPanel account&#39;s email directory. * &#x60;public_html&#x60; — The cPanel account&#39;s web directory. * &#x60;public_ftp&#x60; — The cPanel account&#39;s FTP directory. | [optional] 
**message** | **str** | Short description of the path | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20065_result_data import InlineResponse20065ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20065ResultData from a JSON string
inline_response20065_result_data_instance = InlineResponse20065ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20065ResultData.to_json())

# convert the object into a dict
inline_response20065_result_data_dict = inline_response20065_result_data_instance.to_dict()
# create an instance of InlineResponse20065ResultData from a dict
inline_response20065_result_data_from_dict = InlineResponse20065ResultData.from_dict(inline_response20065_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



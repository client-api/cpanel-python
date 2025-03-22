# InlineResponse200248ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the server&#39;s FTP daemon is enabled.  * &#x60;1&#x60; – Enabled. * &#x60;0&#x60; – Disabled. | [optional] 
**name** | **str** | The FTP server&#39;s name.  * &#x60;pure-ftpd&#x60; * &#x60;proftpd&#x60; * An empty string. | [optional] 
**supports** | [**InlineResponse200248ResultDataSupports**](InlineResponse200248ResultDataSupports.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200248_result_data import InlineResponse200248ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200248ResultData from a JSON string
inline_response200248_result_data_instance = InlineResponse200248ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200248ResultData.to_json())

# convert the object into a dict
inline_response200248_result_data_dict = inline_response200248_result_data_instance.to_dict()
# create an instance of InlineResponse200248ResultData from a dict
inline_response200248_result_data_from_dict = InlineResponse200248ResultData.from_dict(inline_response200248_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



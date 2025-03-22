# InlineResponse200253ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homedir** | **str** | The absolute path to the FTP account&#39;s document root. | [optional] 
**type** | **str** | The type of FTP account.  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60; | [optional] 
**user** | **str** | The username for an FTP account on the cPanel account. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200253_result_data import InlineResponse200253ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200253ResultData from a JSON string
inline_response200253_result_data_instance = InlineResponse200253ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200253ResultData.to_json())

# convert the object into a dict
inline_response200253_result_data_dict = inline_response200253_result_data_instance.to_dict()
# create an instance of InlineResponse200253ResultData from a dict
inline_response200253_result_data_from_dict = InlineResponse200253ResultData.from_dict(inline_response200253_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



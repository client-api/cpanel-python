# InlineResponse200347ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_database_name_length** | **int** | The maximum length of a MySQL database name. | [optional] 
**max_username_length** | **int** | The maximum length of a MySQL database user&#39;s name. | [optional] 
**prefix** | **str** | The account&#39;s database prefix, if database prefixing is enabled. * If database prefixing is enabled, a string of up to the first eight characters of the cPanel account username, and an underscore (_). * If database prefixing is disabled, this is null. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200347_result_data import InlineResponse200347ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200347ResultData from a JSON string
inline_response200347_result_data_instance = InlineResponse200347ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200347ResultData.to_json())

# convert the object into a dict
inline_response200347_result_data_dict = inline_response200347_result_data_instance.to_dict()
# create an instance of InlineResponse200347ResultData from a dict
inline_response200347_result_data_from_dict = InlineResponse200347ResultData.from_dict(inline_response200347_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200355ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_text** | **str** | The message&#39;s contents. | [optional] 
**msg_type** | **str** | The type of message.  * &#x60;status&#x60; * &#x60;error&#x60; * &#x60;info&#x60; * &#x60;note&#x60; * &#x60;warning&#x60;  **Note:**  For more information, read [MySQL&#39;s REPAIR TABLE](http://dev.mysql.com/doc/refman/5.7/en/repair-table.html) documentation. | [optional] 
**table** | **str** | The table&#39;s name in the database. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200355_result_data import InlineResponse200355ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200355ResultData from a JSON string
inline_response200355_result_data_instance = InlineResponse200355ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200355ResultData.to_json())

# convert the object into a dict
inline_response200355_result_data_dict = inline_response200355_result_data_instance.to_dict()
# create an instance of InlineResponse200355ResultData from a dict
inline_response200355_result_data_from_dict = InlineResponse200355ResultData.from_dict(inline_response200355_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200359ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**InlineResponse200359ResultDataDatabase**](InlineResponse200359ResultDataDatabase.md) |  | [optional] 
**database_user** | [**InlineResponse200359ResultDataDatabaseUser**](InlineResponse200359ResultDataDatabaseUser.md) |  | [optional] 
**database_user_password** | **str** | A randomly generated password intended to be maximally randomized. | [optional] 
**hostname** | [**InlineResponse200359ResultDataHostname**](InlineResponse200359ResultDataHostname.md) |  | [optional] 
**port** | **str** | The port to connect to from within the server to connect to the MySQL server | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200359_result_data import InlineResponse200359ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200359ResultData from a JSON string
inline_response200359_result_data_instance = InlineResponse200359ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200359ResultData.to_json())

# convert the object into a dict
inline_response200359_result_data_dict = inline_response200359_result_data_instance.to_dict()
# create an instance of InlineResponse200359ResultData from a dict
inline_response200359_result_data_from_dict = InlineResponse200359ResultData.from_dict(inline_response200359_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



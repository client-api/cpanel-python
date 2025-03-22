# InlineResponse200559ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**List[InlineResponse200559ResultDataAvailable]**](InlineResponse200559ResultDataAvailable.md) | An array of objects containing a list of the WordPress site&#39;s backups. | [optional] 
**dir** | **str** | The absolute path to the backup directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200559_result_data import InlineResponse200559ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200559ResultData from a JSON string
inline_response200559_result_data_instance = InlineResponse200559ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200559ResultData.to_json())

# convert the object into a dict
inline_response200559_result_data_dict = inline_response200559_result_data_instance.to_dict()
# create an instance of InlineResponse200559ResultData from a dict
inline_response200559_result_data_from_dict = InlineResponse200559ResultData.from_dict(inline_response200559_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



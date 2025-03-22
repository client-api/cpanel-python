# InlineResponse200239ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dirs** | [**List[InlineResponse200239ResultDataDirs]**](InlineResponse200239ResultDataDirs.md) | An array of objects containing information about each directory. | [optional] 
**files** | [**List[InlineResponse200239ResultDataFiles]**](InlineResponse200239ResultDataFiles.md) | An array of objects containing information about each file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200239_result_data import InlineResponse200239ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200239ResultData from a JSON string
inline_response200239_result_data_instance = InlineResponse200239ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200239ResultData.to_json())

# convert the object into a dict
inline_response200239_result_data_dict = inline_response200239_result_data_instance.to_dict()
# create an instance of InlineResponse200239ResultData from a dict
inline_response200239_result_data_from_dict = InlineResponse200239ResultData.from_dict(inline_response200239_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



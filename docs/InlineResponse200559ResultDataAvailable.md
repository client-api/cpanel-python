# InlineResponse200559ResultDataAvailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | The date and time the system created the backup. | [optional] 
**file** | **str** | The backup&#39;s file name with the &#x60;tar.zip&#x60; extension. | [optional] 
**path** | **str** | The absolute path to the backup file. | [optional] 
**site** | **str** | The site&#39;s URL **without** the protocol prefix. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200559_result_data_available import InlineResponse200559ResultDataAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200559ResultDataAvailable from a JSON string
inline_response200559_result_data_available_instance = InlineResponse200559ResultDataAvailable.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200559ResultDataAvailable.to_json())

# convert the object into a dict
inline_response200559_result_data_available_dict = inline_response200559_result_data_available_instance.to_dict()
# create an instance of InlineResponse200559ResultDataAvailable from a dict
inline_response200559_result_data_available_from_dict = InlineResponse200559ResultDataAvailable.from_dict(inline_response200559_result_data_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



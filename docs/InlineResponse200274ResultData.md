# InlineResponse200274ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** | The publicly-available URL to which the application will redirect visitors. | [optional] 
**url** | **str** | The publicly-available URL to which the application redirects visitors if the &#x60;redirect_url&#x60; location is unavailable. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200274_result_data import InlineResponse200274ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200274ResultData from a JSON string
inline_response200274_result_data_instance = InlineResponse200274ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200274ResultData.to_json())

# convert the object into a dict
inline_response200274_result_data_dict = inline_response200274_result_data_instance.to_dict()
# create an instance of InlineResponse200274ResultData from a dict
inline_response200274_result_data_from_dict = InlineResponse200274ResultData.from_dict(inline_response200274_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



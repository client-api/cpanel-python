# InlineResponse200555ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayname** | **str** | The webmail client name, as it will display in the interface. | [optional] 
**icon** | **str** | An icon file&#39;s path, relative to the &#x60;/usr/local/cpanel/base/frontend&#x60; directory. | [optional] 
**id** | **str** | The webmail client&#39;s ID. | [optional] 
**url** | **str** | The webmail client&#39;s URL. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200555_result_data import InlineResponse200555ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200555ResultData from a JSON string
inline_response200555_result_data_instance = InlineResponse200555ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200555ResultData.to_json())

# convert the object into a dict
inline_response200555_result_data_dict = inline_response200555_result_data_instance.to_dict()
# create an instance of InlineResponse200555ResultData from a dict
inline_response200555_result_data_from_dict = InlineResponse200555ResultData.from_dict(inline_response200555_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



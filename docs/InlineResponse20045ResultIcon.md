# InlineResponse20045ResultIcon

The application's icon information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | The application&#39;s icon&#39;s height, in pixels. | [optional] 
**url** | **str** | The file path or URL location of the application&#39;s icon. | [optional] 
**width** | **int** | The application&#39;s icon&#39;s width, in pixels. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20045_result_icon import InlineResponse20045ResultIcon

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20045ResultIcon from a JSON string
inline_response20045_result_icon_instance = InlineResponse20045ResultIcon.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20045ResultIcon.to_json())

# convert the object into a dict
inline_response20045_result_icon_dict = inline_response20045_result_icon_instance.to_dict()
# create an instance of InlineResponse20045ResultIcon from a dict
inline_response20045_result_icon_from_dict = InlineResponse20045ResultIcon.from_dict(inline_response20045_result_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



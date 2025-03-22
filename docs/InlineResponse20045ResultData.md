# InlineResponse20045ResultData

An object containing information about the queried `app_keys` application.  **Note:**  The object's name is the value specified in the `app_keys` parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**InlineResponse20045ResultCondition**](InlineResponse20045ResultCondition.md) |  | [optional] 
**description** | **str** | The application&#39;s display name. | [optional] 
**icon** | [**InlineResponse20045ResultIcon**](InlineResponse20045ResultIcon.md) |  | [optional] 
**implements** | **str** | The module namespace for the specific application. | [optional] 
**key** | **str** | The application&#39;s Appkey name. | [optional] 
**name** | **str** | The application&#39;s name. | [optional] 
**order** | **int** | The application&#39;s order in the &#x60;sitemap.json&#x60; file. This value represents the application&#39;s display order in cPanel&#39;s *Home* interface. | [optional] 
**terms** | **List[str]** | Search keywords for the application. | [optional] 
**type** | **str** | The application&#39;s type.  &#x60;item&#x60; is the only possible value. | [optional] 
**url** | **str** | The file path or URL to the the application&#39;s file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20045_result_data import InlineResponse20045ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20045ResultData from a JSON string
inline_response20045_result_data_instance = InlineResponse20045ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20045ResultData.to_json())

# convert the object into a dict
inline_response20045_result_data_dict = inline_response20045_result_data_instance.to_dict()
# create an instance of InlineResponse20045ResultData from a dict
inline_response20045_result_data_from_dict = InlineResponse20045ResultData.from_dict(inline_response20045_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



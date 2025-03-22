# InlineResponse20043ResultData

The feature's details. The function returns an object for each application feature.  **Note:***  The property name corresponds to the name(s) specified in the `app_keys` parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | The feature name. The item will **only** display if the cPanel user has access to this feature. | [optional] 
**file** | **str** | The application&#39;s icon&#39;s filename. | [optional] 
**group** | **str** | The item&#39;s group. | [optional] 
**height** | **int** | The application&#39;s icon&#39;s height, in pixels. | [optional] 
**var_if** | **str** | Conditional arguments that determine whether to display the item, if any exist.  For example, &#x60;$isreseller&#x60; indicates that the item **only** displays for reseller accounts.  For more information, read our [Guide to cPanel Variables](https://go.cpanel.net/guidetovariables) documentation. | [optional] 
**imgtype** | **str** | The item&#39;s image type.  * &#x60;icon&#x60; is the only possible value. | [optional] 
**implements** | **str** | The &#x60;implements&#x60; value for the application. This corresponds to the &#x60;implements&#x60; field in the &#x60;dynamicui.conf&#x60; file. | [optional] 
**itemdesc** | **str** | The application&#39;s display name. value. | [optional] 
**itemorder** | **int** | The application&#39;s order in the &#x60;dynamicui.conf&#x60; file, representing the application&#39;s display order in cPanel&#39;s *Home* interface.  For example, the first item on the cPanel *Home* interface has an &#x60;itemorder&#x60; value of &#x60;1&#x60;. | [optional] 
**searchtext** | **str** | A space-separated list of search terms. The item will display when users enter these search terms in the *Quick Find* textbox. | [optional] 
**subtype** | **str** | The item&#39;s subtype.  * &#x60;img&#x60; is the only possible value. | [optional] 
**touch** | **str** | Conditional arguments that determine whether to display the item, if the touch file exists. | [optional] 
**type** | **str** | The application&#39;s type.  * &#x60;image&#x60; is the only possible value. | [optional] 
**url** | **str** | The location to which the application&#39;s icon links. | [optional] 
**width** | **int** | The application&#39;s icon&#39;s width. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20043_result_data import InlineResponse20043ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20043ResultData from a JSON string
inline_response20043_result_data_instance = InlineResponse20043ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20043ResultData.to_json())

# convert the object into a dict
inline_response20043_result_data_dict = inline_response20043_result_data_instance.to_dict()
# create an instance of InlineResponse20043ResultData from a dict
inline_response20043_result_data_from_dict = InlineResponse20043ResultData.from_dict(inline_response20043_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



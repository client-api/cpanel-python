# InlineResponse20044ResultDataItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acontent** | **str** | The content of a tag in the application&#39;s link. | [optional] 
**base64_png_image** | **str** | The application&#39;s icon in Base64 format. | [optional] 
**feature** | **str** | A feature name. The icon **only** displays if the cPanel user can access this feature. | [optional] 
**file** | **str** | The application&#39;s icon&#39;s filename. | [optional] 
**group** | **str** | The item&#39;s group. | [optional] 
**height** | **str** | The application icon height, in pixels. | [optional] 
**var_if** | **str** | An expression containing cPanel variables that determine whether to display the item. The function **only** returns this value if any variables exist.  For example, &#x60;$isreseller&#x60; indicates that the item **only** displays for reseller accounts.  For more information, read our [Guide to cPanel Variables documentation](https://go.cpanel.net/guidetovariables). | [optional] 
**imgtype** | **str** | The item&#39;s image type.  &#x60;icon&#x60; is the only possible value. | [optional] 
**implements** | **str** | The &#x60;implements&#x60; name of the application. WHM API 1&#39;s &#x60;create_user_session&#x60; and &#x60;get_users_links&#x60; functions use this value. | [optional] 
**itemdesc** | **str** | The application&#39;s display name. | [optional] 
**itemorder** | **str** | The application&#39;s order in the &#x60;dynamicui.conf&#x60; file. This value represents the application&#39;s display order in cPanel&#39;s *Home* interface. | [optional] 
**module** | **str** | The Perl module that the application requires. | [optional] 
**onclick** | **str** | JavaScript function that the browser calls before or instead of URL navigation. | [optional] 
**searchtext** | **str** | One or more space-separated search terms.  The icon will display when users enter these search terms in the *Quick Find* text box in the cPanel interface. | [optional] 
**subtype** | **str** | The item&#39;s subtype.  &#x60;img&#x60; is the only possible value. | [optional] 
**target** | **str** | The target of the application&#39;s link. | [optional] 
**touch** | **str** | Conditional arguments that determine whether to display the item, if a specified touch file exists. | [optional] 
**type** | **str** | The application&#39;s type.  &#x60;image&#x60; is the only possible value. | [optional] 
**url** | **str** | The path to which the application&#39;s icon links. | [optional] 
**width** | **str** | The application&#39;s icon&#39;s width, in pixels. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20044_result_data_items import InlineResponse20044ResultDataItems

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20044ResultDataItems from a JSON string
inline_response20044_result_data_items_instance = InlineResponse20044ResultDataItems.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20044ResultDataItems.to_json())

# convert the object into a dict
inline_response20044_result_data_items_dict = inline_response20044_result_data_items_instance.to_dict()
# create an instance of InlineResponse20044ResultDataItems from a dict
inline_response20044_result_data_items_from_dict = InlineResponse20044ResultDataItems.from_dict(inline_response20044_result_data_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



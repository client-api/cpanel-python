# InlineResponse20042ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | The application&#39;s feature name. The &#x60;app_key&#x60; parameter&#39;s value. | [optional] 
**file** | **str** | The application&#39;s icon&#39;s filename. | [optional] 
**group** | **str** | The application&#39;s group. | [optional] 
**height** | **int** | The application&#39;s icon&#39;s height, in pixels. | [optional] 
**var_if** | **str** | Conditional arguments that determine whether to display the item, if any exist. Conditional arguments that determine whether to display the item. For example, $isreseller indicates that the item only displays for reseller accounts. For more information, read our Guide to cPanel Variables documentation. | [optional] 
**imgtype** | **str** | The item&#39;s image type.  &#x60;icon&#x60; is the only possible value. | [optional] 
**itemdesc** | **str** | The application&#39;s display name. | [optional] 
**itemorder** | **int** | The application&#39;s order in the &#x60;dynamicui.conf&#x60; file representing the application&#39;s display order in cPanel&#39;s Home interface. For example, the first item on the cPanel Home interface has an &#x60;itemorder&#x60; value of &#x60;1&#x60;. | [optional] 
**module** | **str** | The application&#39;s module. A valid module name. | [optional] 
**searchtext** | **str** | One or more search terms. The application&#39;s icon will display when users enter these search terms in the Quick Find text box. A space-separated list of search terms. | [optional] 
**subtype** | **str** | The item&#39;s subtype.  &#x60;img&#x60; is the only possible value . | [optional] 
**type** | **str** | The application&#39;s type.  &#x60;image&#x60; is the only possible value. | [optional] 
**url** | **str** | The location to which the application&#39;s icon links. A valid filepath or URL. | [optional] 
**width** | **int** | The application&#39;s icon&#39;s width representing an image width, in pixels. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20042_result_data import InlineResponse20042ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20042ResultData from a JSON string
inline_response20042_result_data_instance = InlineResponse20042ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20042ResultData.to_json())

# convert the object into a dict
inline_response20042_result_data_dict = inline_response20042_result_data_instance.to_dict()
# create an instance of InlineResponse20042ResultData from a dict
inline_response20042_result_data_from_dict = InlineResponse20042ResultData.from_dict(inline_response20042_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



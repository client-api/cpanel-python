# InlineResponse200469ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**InlineResponse200469ResultMeta**](InlineResponse200469ResultMeta.md) |  | [optional] 
**path** | **str** | The template directory path.  **Note:**    The template directory&#39;s location depends on whether the &#x60;root&#x60; user or a reseller owns the template. | [optional] 
**preview** | **int** | Whether the template includes a preview image. * &#x60;1&#x60; - The template directory contains a &#x60;preview.png&#x60; file. * &#x60;0&#x60; - The template directory does **not** contain a &#x60;preview.png&#x60; file. The cPanel interface will display a placeholder image for this template. | [optional] 
**template** | **str** | The template&#39;s name. This is the name of a directory that contains a &#x60;meta.json&#x60; template information file and exists within one of the following directories: * &#x60;/var/cpanel/customizations/site_templates/&#x60; — The &#x60;root&#x60; user&#39;s templates. * &#x60;/home/username/var/cpanel/reseller/site_templates/&#x60; — A reseller&#39;s templates, where &#x60;username&#x60; represents the reseller&#39;s username. * &#x60;/usr/local/cpanel/3rdparty/share/site_templates/&#x60; — cPanel-provided templates.  **Note:**    The template directory&#39;s location depends on whether the &#x60;root&#x60; user or a reseller owns the template. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200469_result_data import InlineResponse200469ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200469ResultData from a JSON string
inline_response200469_result_data_instance = InlineResponse200469ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200469ResultData.to_json())

# convert the object into a dict
inline_response200469_result_data_dict = inline_response200469_result_data_instance.to_dict()
# create an instance of InlineResponse200469ResultData from a dict
inline_response200469_result_data_from_dict = InlineResponse200469ResultData.from_dict(inline_response200469_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200470ResultTemplateSettings

An object containing template settings.  **Important:**  This object also contains the user's website content. The template provider determines these values.   * For information about the content for cPanel-provided templates, read our [Guide to Site Publisher Templates](https://go.cpanel.net/SitePublisherTemplates) documentation.   * For more information about other templates, contact the template provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_empty** | **int** | Whether the domain&#39;s &#x60;configurations.json&#x60; file exists and contains template information. * &#x60;1&#x60; — The &#x60;configurations.json&#x60; file exists and contains template information. * &#x60;0&#x60; — The &#x60;configurations.json&#x60; file does not exist, or does not contain template information. | [optional] 
**path** | **str** | The template directory path. * &#x60;/var/cpanel/customizations/site_templates/&#x60; — The &#x60;root&#x60; user&#39;s templates. * &#x60;/home/username/var/cpanel/reseller/site_templates/&#x60; — A reseller&#39;s templates, where username represents the reseller&#39;s &#x60;username&#x60;. * &#x60;/usr/local/cpanel/3rdparty/share/site_templates/&#x60; — cPanel-provided templates. | [optional] 
**template** | **str** | The template&#39;s name as it appears in the &#x60;configurations.json&#x60; file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200470_result_template_settings import InlineResponse200470ResultTemplateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200470ResultTemplateSettings from a JSON string
inline_response200470_result_template_settings_instance = InlineResponse200470ResultTemplateSettings.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200470ResultTemplateSettings.to_json())

# convert the object into a dict
inline_response200470_result_template_settings_dict = inline_response200470_result_template_settings_instance.to_dict()
# create an instance of InlineResponse200470ResultTemplateSettings from a dict
inline_response200470_result_template_settings_from_dict = InlineResponse200470ResultTemplateSettings.from_dict(inline_response200470_result_template_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



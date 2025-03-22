# InlineResponse200588ResultDataValueInnerOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | An array of information that corresponds with a text value.  **Note:**  The function **only** returns this value if one exists. | [optional] 
**level** | **str** | The level that triggers a recommendation to appear, based on [Bootstrap 3 alert components](http://getbootstrap.com/components/#alerts).  * &#x60;primary&#x60; * &#x60;success&#x60; * &#x60;info&#x60; * &#x60;warning&#x60; * &#x60;danger&#x60;  **Note:**  * The function **only** returns this value if one exists. * This return&#39;s value only affects the UI if set to &#x60;danger&#x60;. | [optional] 
**recommended** | **bool** | The type of recommendation that the interface will return.  * &#x60;true&#x60; - Recommended. * &#x60;false&#x60; - Not recommended.  **Note:**  * The function **only** returns this value if one exists. * If the function does **not** return this value, then the interface will display informational text. | [optional] 
**text** | **str** | The text that the user interface displays. | [optional] 
**url** | **str** | A URL that provides more information.  **Note:**  The function **only** returns this value if one exists. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200588_result_data_value_inner_options_inner import InlineResponse200588ResultDataValueInnerOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200588ResultDataValueInnerOptionsInner from a JSON string
inline_response200588_result_data_value_inner_options_inner_instance = InlineResponse200588ResultDataValueInnerOptionsInner.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200588ResultDataValueInnerOptionsInner.to_json())

# convert the object into a dict
inline_response200588_result_data_value_inner_options_inner_dict = inline_response200588_result_data_value_inner_options_inner_instance.to_dict()
# create an instance of InlineResponse200588ResultDataValueInnerOptionsInner from a dict
inline_response200588_result_data_value_inner_options_inner_from_dict = InlineResponse200588ResultDataValueInnerOptionsInner.from_dict(inline_response200588_result_data_value_inner_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



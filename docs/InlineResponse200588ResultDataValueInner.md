# InlineResponse200588ResultDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** | The recommendation&#39;s description.  **Note:**  The function **only** returns this value if one exists. | [optional] 
**level** | **str** | The level that triggers a recommendation to appear, based on [Bootstrap 3 alert components](http://getbootstrap.com/components/#alerts).  * &#x60;primary&#x60; * &#x60;success&#x60; * &#x60;info&#x60; * &#x60;warning&#x60; * &#x60;danger&#x60;  **Note:**  * The function **only** returns this value if one exists. * This return&#39;s value only affects the UI if set to &#x60;danger&#x60;. | [optional] 
**name** | **str** | The recommendation&#39;s name. | [optional] 
**on** | **str** | The action that triggers a recommendation.  * &#x60;add&#x60; * &#x60;remove&#x60; | [optional] 
**options** | [**List[InlineResponse200588ResultDataValueInnerOptionsInner]**](InlineResponse200588ResultDataValueInnerOptionsInner.md) | An object that contains each option for the package&#39;s recommendations. | [optional] 
**url** | **str** | A URL to provide more information.  **Note:**  The function **only** returns this value if one exists. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200588_result_data_value_inner import InlineResponse200588ResultDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200588ResultDataValueInner from a JSON string
inline_response200588_result_data_value_inner_instance = InlineResponse200588ResultDataValueInner.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200588ResultDataValueInner.to_json())

# convert the object into a dict
inline_response200588_result_data_value_inner_dict = inline_response200588_result_data_value_inner_instance.to_dict()
# create an instance of InlineResponse200588ResultDataValueInner from a dict
inline_response200588_result_data_value_inner_from_dict = InlineResponse200588ResultDataValueInner.from_dict(inline_response200588_result_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse20045ResultCondition

An object containing the application's conditions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | The feature that the user must have access to in order to see the application in their cPanel *Home* interface. | [optional] 
**var_if** | **str** | cPanel variables that determine whether to display the item, if any exist.  For example, &#x60;$isreseller&#x60; indicates that the item **only** displays for reseller accounts.  For more information, read our [Guide to cPanel Variables](https://go.cpanel.net/guidetovariables) documentation. | [optional] 
**module** | **str** | The name of the module that provides the application. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20045_result_condition import InlineResponse20045ResultCondition

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20045ResultCondition from a JSON string
inline_response20045_result_condition_instance = InlineResponse20045ResultCondition.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20045ResultCondition.to_json())

# convert the object into a dict
inline_response20045_result_condition_dict = inline_response20045_result_condition_instance.to_dict()
# create an instance of InlineResponse20045ResultCondition from a dict
inline_response20045_result_condition_from_dict = InlineResponse20045ResultCondition.from_dict(inline_response20045_result_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200183ResultActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The filter’s action.  Some common ones include:  * &#x60;deliver&#x60; — The filter sends mail to the dest address. * &#x60;fail&#x60; — The filter forces a delivery failure. * &#x60;finish&#x60; — The filter stops message processing. * &#x60;save&#x60; — The filter saves mail to the dest file. * &#x60;pipe&#x60; — The filter sends mail to the dest application.  For more information, read [Exim’s _Filter commands_ documentation](http://www.exim.org/exim-html-3.30/doc/html/filter_11.html). | [optional] 
**dest** | **str** | The destination to which the filter sends mail. * A file path. * An application path. * A valid email address. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200183_result_actions import InlineResponse200183ResultActions

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200183ResultActions from a JSON string
inline_response200183_result_actions_instance = InlineResponse200183ResultActions.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200183ResultActions.to_json())

# convert the object into a dict
inline_response200183_result_actions_dict = inline_response200183_result_actions_instance.to_dict()
# create an instance of InlineResponse200183ResultActions from a dict
inline_response200183_result_actions_from_dict = InlineResponse200183ResultActions.from_dict(inline_response200183_result_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200326ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_null** | **int** | Whether the domain allows hotlinks from an empty or null referral URL. * &#x60;1&#x60; - Allows hotlinks. * &#x60;0&#x60; - Does not allow hotlinks. | [optional] 
**extensions** | **str** | A comma-separated list of file types to hotlink protect. | [optional] 
**redirect_url** | **str** | The URL to which to send hotlinkers. | [optional] 
**state** | **str** | Whether hotlink protection is enabled.  * &#x60;enabled&#x60; * &#x60;disabled&#x60; | [optional] 
**urls** | **List[str]** | An array of the domains with hotlink protection. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200326_result_data import InlineResponse200326ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200326ResultData from a JSON string
inline_response200326_result_data_instance = InlineResponse200326ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200326ResultData.to_json())

# convert the object into a dict
inline_response200326_result_data_dict = inline_response200326_result_data_instance.to_dict()
# create an instance of InlineResponse200326ResultData from a dict
inline_response200326_result_data_from_dict = InlineResponse200326ResultData.from_dict(inline_response200326_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



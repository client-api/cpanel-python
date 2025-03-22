# InlineResponse200305ResultDataActionUrls

An object that contains actionable URLs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ev_click_through_status** | **str** | A URL that a user can use to expedite the validation process for Extended Validation (EV) certificates. | [optional] 
**ov_callback_status** | **str** | A URL that a user can use to expedite the validation process for Organization Validated (OV) certificates. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200305_result_data_action_urls import InlineResponse200305ResultDataActionUrls

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200305ResultDataActionUrls from a JSON string
inline_response200305_result_data_action_urls_instance = InlineResponse200305ResultDataActionUrls.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200305ResultDataActionUrls.to_json())

# convert the object into a dict
inline_response200305_result_data_action_urls_dict = inline_response200305_result_data_action_urls_instance.to_dict()
# create an instance of InlineResponse200305ResultDataActionUrls from a dict
inline_response200305_result_data_action_urls_from_dict = InlineResponse200305ResultDataActionUrls.from_dict(inline_response200305_result_data_action_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



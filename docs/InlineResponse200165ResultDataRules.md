# InlineResponse200165ResultDataRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **str** | The filter&#39;s match type.  * &#x60;is&#x60; * &#x60;matches&#x60; * &#x60;contains&#x60; * &#x60;does not contain&#x60; * &#x60;begins&#x60; * &#x60;does not begin&#x60; * &#x60;ends&#x60; * &#x60;does not end&#x60; * &#x60;does not match&#x60; * &#x60;is above&#x60; * &#x60;is not above&#x60; * &#x60;is below&#x60; * &#x60;is not below&#x60; | [optional] 
**number** | **int** | The filter&#39;s position in the order of the account&#39;s filters. | [optional] 
**opt** | **str** | The connection between multiple conditions. * &#x60;and&#x60; -  Match both conditions. * &#x60;or&#x60; -  Match either condition. * &#x60;null&#x60; -  There is only one condition. | [optional] 
**part** | **str** | The queried email section. * &#x60;$header_from:&#x60; -  Matches against the From: section. * &#x60;$header_subject:&#x60; -  Matches against the Subject: section. * &#x60;$header_to:&#x60; -  Matches against the To: section. * &#x60;$reply_address:&#x60; -  Matches against the Reply To: section. * &#x60;$message_body&#x60; -  Matches against the message&#39;s body. * &#x60;$message_headers&#x60; -  Matches against the message&#39;s headers. * &#x60;foranyaddress $h_to:,$h_cc:,$h_bcc:&#x60; -  Matches against all message recipients. * &#x60;not delivered&#x60; -  Matches if the message is not queued for delivery. * &#x60;error_message&#x60; -  Matches if the incoming message bounced. | [optional] 
**val** | **str** | The matched value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200165_result_data_rules import InlineResponse200165ResultDataRules

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200165ResultDataRules from a JSON string
inline_response200165_result_data_rules_instance = InlineResponse200165ResultDataRules.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200165ResultDataRules.to_json())

# convert the object into a dict
inline_response200165_result_data_rules_dict = inline_response200165_result_data_rules_instance.to_dict()
# create an instance of InlineResponse200165ResultDataRules from a dict
inline_response200165_result_data_rules_from_dict = InlineResponse200165ResultDataRules.from_dict(inline_response200165_result_data_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



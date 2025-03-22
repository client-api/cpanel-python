# InlineResponse200183ResultRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **str** | The filter’s match type. | [optional] 
**opt** | **str** | The connection between multiple conditions.   * &#x60;and&#x60; — Match both conditions.   * &#x60;or&#x60; — Match either condition.   * &#x60;null&#x60; — Only one condition exists. | [optional] 
**part** | **str** | The queried email section.  Some common ones include:  * &#x60;$header_from:&#x60; — Matches against the &#x60;From:&#x60; section. * &#x60;$header_subject:&#x60; — Matches against the &#x60;Subject:&#x60; section. * &#x60;$header_to:&#x60; — Matches against the &#x60;To:&#x60; section. * &#x60;$reply_address:&#x60; — Matches against the &#x60;Reply To:&#x60; section. * &#x60;$message_body&#x60; — Matches against the message’s body. * &#x60;$message_headers&#x60; — Matches against the message’s headers. * &#x60;foranyaddress $h_to:,$h_cc:,$h_bcc:&#x60; —  Matches against all message recipients. * &#x60;not delivered&#x60; — Matches if the system has not queued the message for delivery. * &#x60;error_message&#x60; — Matches if the incoming message bounced.  For more options, read [Exim’s documentation](https://exim.org/exim-html-3.30/doc/html/filter.html). | [optional] 
**val** | **str** | The matched value. A string value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200183_result_rules import InlineResponse200183ResultRules

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200183ResultRules from a JSON string
inline_response200183_result_rules_instance = InlineResponse200183ResultRules.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200183ResultRules.to_json())

# convert the object into a dict
inline_response200183_result_rules_dict = inline_response200183_result_rules_instance.to_dict()
# create an instance of InlineResponse200183ResultRules from a dict
inline_response200183_result_rules_from_dict = InlineResponse200183ResultRules.from_dict(inline_response200183_result_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



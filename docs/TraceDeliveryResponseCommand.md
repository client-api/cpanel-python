# TraceDeliveryResponseCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The email address of an email message recipient. | [optional] 
**type** | **str** | A type of trace node. The system returns this value to indicate the **end** of routing. * &#x60;bounce&#x60; - The system rejected the email&#39;s delivery. * &#x60;command&#x60; - The system will run a command when it receives an email. * &#x60;defer&#x60; - The system deferred the email. * &#x60;discard&#x60; - The system discarded the email. * &#x60;error&#x60; - The system encountered an error. * &#x60;local_delivery&#x60; - The system sent the email to a local mailbox. * &#x60;remote_delivery&#x60; - The system sent the email via Simple Mail Transfer Protocol (SMTP). * &#x60;routed&#x60; - The system routed the email elsewhere.  **Note:** * The structure of the &#x60;destinations&#x60; return changes depending on the &#x60;type&#x60; return value. * The &#x60;routed&#x60; type can return any other type&#39;s data structure as part of the &#x60;destinations&#x60; return value.  For more information, see the return structure for each &#x60;type&#x60; return value below: | [optional] 
**destinations** | [**TraceDeliveryResponseCommandDestinations**](TraceDeliveryResponseCommandDestinations.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.trace_delivery_response_command import TraceDeliveryResponseCommand

# TODO update the JSON string below
json = "{}"
# create an instance of TraceDeliveryResponseCommand from a JSON string
trace_delivery_response_command_instance = TraceDeliveryResponseCommand.from_json(json)
# print the JSON string representation of the object
print(TraceDeliveryResponseCommand.to_json())

# convert the object into a dict
trace_delivery_response_command_dict = trace_delivery_response_command_instance.to_dict()
# create an instance of TraceDeliveryResponseCommand from a dict
trace_delivery_response_command_from_dict = TraceDeliveryResponseCommand.from_dict(trace_delivery_response_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



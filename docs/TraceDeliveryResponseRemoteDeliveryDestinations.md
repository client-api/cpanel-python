# TraceDeliveryResponseRemoteDeliveryDestinations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mx** | **List[str]** | An array of strings containing [mail exchanger (MX) information](https://en.wikipedia.org/wiki/MX_record).  Each string contains information for a single mail exchanger (MX), including:  * The server&#39;s hostname.  * The server&#39;s resolving IP address.  * The MX record&#39;s priority. The lower the value, the higher its priority.  * Whether DNSSEC is enabled for the hostname. | [optional] 
**type** | **str** | A type of trace node. The system returns this value to indicate the **end** of routing. * &#x60;bounce&#x60; - The system rejected the email&#39;s delivery. * &#x60;command&#x60; - The system will run a command when it receives an email. * &#x60;defer&#x60; - The system deferred the email. * &#x60;discard&#x60; - The system discarded the email. * &#x60;error&#x60; - The system encountered an error. * &#x60;local_delivery&#x60; - The system sent the email to a local mailbox. * &#x60;remote_delivery&#x60; - The system sent the email via Simple Mail Transfer Protocol (SMTP). * &#x60;routed&#x60; - The system routed the email elsewhere.  **Note:** * The structure of the &#x60;destinations&#x60; return changes depending on the &#x60;type&#x60; return value. * The &#x60;routed&#x60; type can return any other type&#39;s data structure as part of the &#x60;destinations&#x60; return value. | [optional] 

## Example

```python
from clientapi_cpanel.models.trace_delivery_response_remote_delivery_destinations import TraceDeliveryResponseRemoteDeliveryDestinations

# TODO update the JSON string below
json = "{}"
# create an instance of TraceDeliveryResponseRemoteDeliveryDestinations from a JSON string
trace_delivery_response_remote_delivery_destinations_instance = TraceDeliveryResponseRemoteDeliveryDestinations.from_json(json)
# print the JSON string representation of the object
print(TraceDeliveryResponseRemoteDeliveryDestinations.to_json())

# convert the object into a dict
trace_delivery_response_remote_delivery_destinations_dict = trace_delivery_response_remote_delivery_destinations_instance.to_dict()
# create an instance of TraceDeliveryResponseRemoteDeliveryDestinations from a dict
trace_delivery_response_remote_delivery_destinations_from_dict = TraceDeliveryResponseRemoteDeliveryDestinations.from_dict(trace_delivery_response_remote_delivery_destinations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



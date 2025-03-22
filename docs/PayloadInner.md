# PayloadInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_index** | **int** | The line’s index in the zone file. | [optional] 
**type** | **str** | The type of object in the zone file:  * &#x60;record&#x60; - A resource record. * &#x60;control&#x60; - A control statement. * &#x60;comment&#x60; - A line comment. | [optional] 
**data_b64** | **List[str]** | The resource record’s content, encoded to base64. | [optional] 
**dname_b64** | **str** | The resource record’s owner, encoded to base64. A base64-decoded owner that lacks a trailing period (&#x60;.&#x60;) is a subdomain of the zone. | [optional] 
**record_type** | **str** | The resource record’s type. | [optional] 
**ttl** | **int** | The resource record’s TTL (Time-to-Live). | [optional] 
**text_b64** | **str** | The line’s text, encoded to base64. | [optional] 

## Example

```python
from clientapi_cpanel.models.payload_inner import PayloadInner

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadInner from a JSON string
payload_inner_instance = PayloadInner.from_json(json)
# print the JSON string representation of the object
print(PayloadInner.to_json())

# convert the object into a dict
payload_inner_dict = payload_inner_instance.to_dict()
# create an instance of PayloadInner from a dict
payload_inner_from_dict = PayloadInner.from_dict(payload_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponseRR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_index** | **int** | The line’s index in the zone file. | [optional] 
**type** | **str** | The type of object in the zone file:  * &#x60;record&#x60; - A resource record. * &#x60;control&#x60; - A control statement. * &#x60;comment&#x60; - A line comment. | [optional] 
**data_b64** | **List[str]** | The resource record’s content, encoded to base64. | [optional] 
**dname_b64** | **str** | The resource record’s owner, encoded to base64. A base64-decoded owner that lacks a trailing period (&#x60;.&#x60;) is a subdomain of the zone. | [optional] 
**record_type** | **str** | The resource record’s type. | [optional] 
**ttl** | **int** | The resource record’s TTL (Time-to-Live). | [optional] 

## Example

```python
from clientapi_cpanel.models.response_rr import ResponseRR

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseRR from a JSON string
response_rr_instance = ResponseRR.from_json(json)
# print the JSON string representation of the object
print(ResponseRR.to_json())

# convert the object into a dict
response_rr_dict = response_rr_instance.to_dict()
# create an instance of ResponseRR from a dict
response_rr_from_dict = ResponseRR.from_dict(response_rr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



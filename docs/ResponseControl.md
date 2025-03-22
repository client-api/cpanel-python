# ResponseControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_index** | **int** | The line’s index in the zone file. | [optional] 
**type** | **str** | The type of object in the zone file:  * &#x60;record&#x60; - A resource record. * &#x60;control&#x60; - A control statement. * &#x60;comment&#x60; - A line comment. | [optional] 
**text_b64** | **str** | The line’s text, encoded to base64. | [optional] 

## Example

```python
from clientapi_cpanel.models.response_control import ResponseControl

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseControl from a JSON string
response_control_instance = ResponseControl.from_json(json)
# print the JSON string representation of the object
print(ResponseControl.to_json())

# convert the object into a dict
response_control_dict = response_control_instance.to_dict()
# create an instance of ResponseControl from a dict
response_control_from_dict = ResponseControl.from_dict(response_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



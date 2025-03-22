# ResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_index** | **int** | The line’s index in the zone file. | [optional] 
**type** | **str** | The type of object in the zone file:  * &#x60;record&#x60; - A resource record. * &#x60;control&#x60; - A control statement. * &#x60;comment&#x60; - A line comment. | [optional] 

## Example

```python
from clientapi_cpanel.models.response_base import ResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBase from a JSON string
response_base_instance = ResponseBase.from_json(json)
# print the JSON string representation of the object
print(ResponseBase.to_json())

# convert the object into a dict
response_base_dict = response_base_instance.to_dict()
# create an instance of ResponseBase from a dict
response_base_from_dict = ResponseBase.from_dict(response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



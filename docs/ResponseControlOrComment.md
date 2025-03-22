# ResponseControlOrComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_index** | **int** | The line’s index in the zone file. | [optional] 
**type** | **str** | The type of object in the zone file:  * &#x60;record&#x60; - A resource record. * &#x60;control&#x60; - A control statement. * &#x60;comment&#x60; - A line comment. | [optional] 
**text_b64** | **str** | The line’s text, encoded to base64. | [optional] 

## Example

```python
from clientapi_cpanel.models.response_control_or_comment import ResponseControlOrComment

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseControlOrComment from a JSON string
response_control_or_comment_instance = ResponseControlOrComment.from_json(json)
# print the JSON string representation of the object
print(ResponseControlOrComment.to_json())

# convert the object into a dict
response_control_or_comment_dict = response_control_or_comment_instance.to_dict()
# create an instance of ResponseControlOrComment from a dict
response_control_or_comment_from_dict = ResponseControlOrComment.from_dict(response_control_or_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



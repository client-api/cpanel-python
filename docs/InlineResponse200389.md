# InlineResponse200389


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20033Result**](InlineResponse20033Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200389 import InlineResponse200389

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200389 from a JSON string
inline_response200389_instance = InlineResponse200389.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200389.to_json())

# convert the object into a dict
inline_response200389_dict = inline_response200389_instance.to_dict()
# create an instance of InlineResponse200389 from a dict
inline_response200389_from_dict = InlineResponse200389.from_dict(inline_response200389_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



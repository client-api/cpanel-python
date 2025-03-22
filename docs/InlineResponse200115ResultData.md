# InlineResponse200115ResultData

Information about the deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **float** | Whether a DDNS domain with the given ID existed for deletion.  * &#x60;0&#x60; - No DDNS domain with the given ID existed. * &#x60;1&#x60; - A DDNS domain with the given ID existed but is now deleted. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200115_result_data import InlineResponse200115ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200115ResultData from a JSON string
inline_response200115_result_data_instance = InlineResponse200115ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200115ResultData.to_json())

# convert the object into a dict
inline_response200115_result_data_dict = inline_response200115_result_data_instance.to_dict()
# create an instance of InlineResponse200115ResultData from a dict
inline_response200115_result_data_from_dict = InlineResponse200115ResultData.from_dict(inline_response200115_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



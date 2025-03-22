# InlineResponse200376ResultDataPersonalization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The message that describes the failure if &#x60;success&#x60; returns &#x60;0&#x60;, or &#x60;OK&#x60; if &#x60;success&#x60; returns &#x60;1&#x60;. | [optional] 
**success** | **int** | Whether the function successfully saved the value on the server.   - &#x60;1&#x60; — Successful.   - &#x60;0&#x60; — Unsuccessful. | [optional] 
**value** | **str** | The value stored for the associated NVData key, or a null value if the key does not exist in the store. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200376_result_data_personalization import InlineResponse200376ResultDataPersonalization

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200376ResultDataPersonalization from a JSON string
inline_response200376_result_data_personalization_instance = InlineResponse200376ResultDataPersonalization.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200376ResultDataPersonalization.to_json())

# convert the object into a dict
inline_response200376_result_data_personalization_dict = inline_response200376_result_data_personalization_instance.to_dict()
# create an instance of InlineResponse200376ResultDataPersonalization from a dict
inline_response200376_result_data_personalization_from_dict = InlineResponse200376ResultDataPersonalization.from_dict(inline_response200376_result_data_personalization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



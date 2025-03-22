# InlineResponse200375ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalization** | [**Dict[str, InlineResponse200375ResultDataPersonalization]**](InlineResponse200375ResultDataPersonalization.md) | The retrieved NVData information stored on the server.  **Note:**  * You set this return&#39;s name based on the keys that you provide in the &#x60;personalization&#x60; parameter with the UAPI &#x60;Personalization::set&#x60; function. * This return&#39;s name is the NVData key&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200375_result_data import InlineResponse200375ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200375ResultData from a JSON string
inline_response200375_result_data_instance = InlineResponse200375ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200375ResultData.to_json())

# convert the object into a dict
inline_response200375_result_data_dict = inline_response200375_result_data_instance.to_dict()
# create an instance of InlineResponse200375ResultData from a dict
inline_response200375_result_data_from_dict = InlineResponse200375ResultData.from_dict(inline_response200375_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



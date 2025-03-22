# InlineResponse200201ResultData

A list of domains and the replaced manual MX redirect entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **str** | The domain for which the function replaced the manual MX redirect entry.  * null — The domain did not have an existing manual MX redirect entry.  **Note:**  This return&#39;s name is the &#x60;domain&#x60; parameter&#39;s value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200201_result_data import InlineResponse200201ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200201ResultData from a JSON string
inline_response200201_result_data_instance = InlineResponse200201ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200201ResultData.to_json())

# convert the object into a dict
inline_response200201_result_data_dict = inline_response200201_result_data_instance.to_dict()
# create an instance of InlineResponse200201ResultData from a dict
inline_response200201_result_data_from_dict = InlineResponse200201ResultData.from_dict(inline_response200201_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



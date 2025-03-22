# InlineResponse200281ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **List[str]** | The available PHP versions.  - &#x60;ea-php72&#x60; - &#x60;ea-php73&#x60; - &#x60;ea-php74&#x60; -  Any custom PHP package name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200281_result_data import InlineResponse200281ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200281ResultData from a JSON string
inline_response200281_result_data_instance = InlineResponse200281ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200281ResultData.to_json())

# convert the object into a dict
inline_response200281_result_data_dict = inline_response200281_result_data_instance.to_dict()
# create an instance of InlineResponse200281ResultData from a dict
inline_response200281_result_data_from_dict = InlineResponse200281ResultData.from_dict(inline_response200281_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



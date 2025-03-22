# InlineResponse200280ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The domains that obtain their PHP version from the PHP configuration. Any valid domain or subdomain.  **Note:**  This function does **not** return parked domains. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200280_result_data import InlineResponse200280ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200280ResultData from a JSON string
inline_response200280_result_data_instance = InlineResponse200280ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200280ResultData.to_json())

# convert the object into a dict
inline_response200280_result_data_dict = inline_response200280_result_data_instance.to_dict()
# create an instance of InlineResponse200280ResultData from a dict
inline_response200280_result_data_from_dict = InlineResponse200280ResultData.from_dict(inline_response200280_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



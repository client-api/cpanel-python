# InlineResponse200331ResultDataOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_domains** | **List[str]** | List of invalid domains provided by caller. | [optional] 
**invalid_domains_provided** | **int** | Indicates caller error on API call. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200331_result_data_one_of1 import InlineResponse200331ResultDataOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200331ResultDataOneOf1 from a JSON string
inline_response200331_result_data_one_of1_instance = InlineResponse200331ResultDataOneOf1.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200331ResultDataOneOf1.to_json())

# convert the object into a dict
inline_response200331_result_data_one_of1_dict = inline_response200331_result_data_one_of1_instance.to_dict()
# create an instance of InlineResponse200331ResultDataOneOf1 from a dict
inline_response200331_result_data_one_of1_from_dict = InlineResponse200331ResultDataOneOf1.from_dict(inline_response200331_result_data_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



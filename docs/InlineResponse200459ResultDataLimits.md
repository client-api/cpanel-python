# InlineResponse200459ResultDataLimits

Restrictions placed on the monitoring checks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_crawl_depth** | **int** | The maximum number of URLs to check for dead links on a page. | [optional] [default to 500]

## Example

```python
from clientapi_cpanel.models.inline_response200459_result_data_limits import InlineResponse200459ResultDataLimits

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200459ResultDataLimits from a JSON string
inline_response200459_result_data_limits_instance = InlineResponse200459ResultDataLimits.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200459ResultDataLimits.to_json())

# convert the object into a dict
inline_response200459_result_data_limits_dict = inline_response200459_result_data_limits_instance.to_dict()
# create an instance of InlineResponse200459ResultDataLimits from a dict
inline_response200459_result_data_limits_from_dict = InlineResponse200459ResultDataLimits.from_dict(inline_response200459_result_data_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200541ResultDataMaximumDeferFailPercentage

The [percentage of failed or deferred email messages](https://go.cpanel.net/howtopreventspam) that the account can send per hour before outgoing mail is rate-limited. * `unlimited` * An integer value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response200541_result_data_maximum_defer_fail_percentage import InlineResponse200541ResultDataMaximumDeferFailPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200541ResultDataMaximumDeferFailPercentage from a JSON string
inline_response200541_result_data_maximum_defer_fail_percentage_instance = InlineResponse200541ResultDataMaximumDeferFailPercentage.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200541ResultDataMaximumDeferFailPercentage.to_json())

# convert the object into a dict
inline_response200541_result_data_maximum_defer_fail_percentage_dict = inline_response200541_result_data_maximum_defer_fail_percentage_instance.to_dict()
# create an instance of InlineResponse200541ResultDataMaximumDeferFailPercentage from a dict
inline_response200541_result_data_maximum_defer_fail_percentage_from_dict = InlineResponse200541ResultDataMaximumDeferFailPercentage.from_dict(inline_response200541_result_data_maximum_defer_fail_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



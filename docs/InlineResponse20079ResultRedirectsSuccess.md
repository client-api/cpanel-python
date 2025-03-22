# InlineResponse20079ResultRedirectsSuccess

Whether the server returns a [2XX HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success). * `1` — The server returns a 2XX status code. * `0` or an empty string — The server does **not** return a 2XX status code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from clientapi_cpanel.models.inline_response20079_result_redirects_success import InlineResponse20079ResultRedirectsSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20079ResultRedirectsSuccess from a JSON string
inline_response20079_result_redirects_success_instance = InlineResponse20079ResultRedirectsSuccess.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20079ResultRedirectsSuccess.to_json())

# convert the object into a dict
inline_response20079_result_redirects_success_dict = inline_response20079_result_redirects_success_instance.to_dict()
# create an instance of InlineResponse20079ResultRedirectsSuccess from a dict
inline_response20079_result_redirects_success_from_dict = InlineResponse20079ResultRedirectsSuccess.from_dict(inline_response20079_result_redirects_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



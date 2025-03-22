# InlineResponse20079ResultRedirects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | A message that explains why the function failed. | [optional] 
**headers** | **object** | An object that contains the [HTTP::Tiny](http://search.cpan.org/~dagolden/HTTP-Tiny-0.070/lib/HTTP/Tiny.pm) CPAN module returns.  **Note:**    This object&#39;s contents vary according to the URL&#39;s headers. | [optional] 
**protocol** | **str** | The URL&#39;s HTTP protocol. | [optional] 
**reason** | **str** | The HTTP response status message. | [optional] 
**redirects** | **List[str]** | An array of objects containing the redirects, if the value exists. | [optional] 
**status** | **int** | The [HTTP response status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). | [optional] 
**success** | [**InlineResponse20079ResultRedirectsSuccess**](InlineResponse20079ResultRedirectsSuccess.md) |  | [optional] 
**url** | **str** | The URL that the function searches for the DCV file. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20079_result_redirects import InlineResponse20079ResultRedirects

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20079ResultRedirects from a JSON string
inline_response20079_result_redirects_instance = InlineResponse20079ResultRedirects.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20079ResultRedirects.to_json())

# convert the object into a dict
inline_response20079_result_redirects_dict = inline_response20079_result_redirects_instance.to_dict()
# create an instance of InlineResponse20079ResultRedirects from a dict
inline_response20079_result_redirects_from_dict = InlineResponse20079ResultRedirects.from_dict(inline_response20079_result_redirects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200476ResultStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_sitejet_published** | **int** | Whether the Sitejet website is published. * &#x60;1&#x60; - Sitejet website is published. * &#x60;0&#x60; - Sitejet website is not published. | [optional] 
**has_sitejet_website** | **int** | Whether the domain&#39;s document root diretory contains a Sitejet directory. * &#x60;1&#x60; - User has created a Sitejet website. * &#x60;0&#x60; - User has not created a Sitejet website. | [optional] 
**is_sitejet** | **int** | Whether the domain&#39;s document root diretory&#39;s &#x60;index.html&#x60; file contains Sitejet deployed content. * &#x60;1&#x60; - User has a Sitejet website. * &#x60;0&#x60; - User does not have a Sitejet website. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200476_result_status import InlineResponse200476ResultStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200476ResultStatus from a JSON string
inline_response200476_result_status_instance = InlineResponse200476ResultStatus.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200476ResultStatus.to_json())

# convert the object into a dict
inline_response200476_result_status_dict = inline_response200476_result_status_instance.to_dict()
# create an instance of InlineResponse200476ResultStatus from a dict
inline_response200476_result_status_from_dict = InlineResponse200476ResultStatus.from_dict(inline_response200476_result_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



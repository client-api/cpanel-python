# InlineResponse200476ResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | The website&#39;s comapany. | [optional] 
**cpanel_domain_guid** | **str** | The cPanel user&#39;s domain. | [optional] 
**fullcms** | **float** | Whether the full Sitejet Content Management System is enabled. * &#x60;1&#x60; - Full CMS is enabled. * &#x60;0&#x60; - Full CMS is disabled. | [optional] 
**language** | **str** | The language selection for the Sitejet Content Management System. | [optional] 
**latest_publish_date** | **int** | The last successful publication of the Sitejet domain in Unix time format. | [optional] 
**publish_status** | **int** | Whether the Sitejet domain is published. * &#x60;1&#x60; - Website is published. * &#x60;0&#x60; - Website is not published. | [optional] 
**website_id** | **int** | The website ID of the created website. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200476_result_metadata import InlineResponse200476ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200476ResultMetadata from a JSON string
inline_response200476_result_metadata_instance = InlineResponse200476ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200476ResultMetadata.to_json())

# convert the object into a dict
inline_response200476_result_metadata_dict = inline_response200476_result_metadata_instance.to_dict()
# create an instance of InlineResponse200476ResultMetadata from a dict
inline_response200476_result_metadata_from_dict = InlineResponse200476ResultMetadata.from_dict(inline_response200476_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InlineResponse200480ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The templates creation date. | [optional] 
**description** | **str** | The template&#39;s description. | [optional] 
**id** | **int** | The template&#39;s ID. | [optional] 
**image** | **str** | The relative path to the template image on the SiteJet CMS website. | [optional] 
**name** | **str** | The template&#39;s name. | [optional] 
**preview_url** | **str** | The website&#39;s preview URL. | [optional] 
**tags** | **List[str]** | The template&#39;s catagory search tags. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200480_result_data import InlineResponse200480ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200480ResultData from a JSON string
inline_response200480_result_data_instance = InlineResponse200480ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200480ResultData.to_json())

# convert the object into a dict
inline_response200480_result_data_dict = inline_response200480_result_data_instance.to_dict()
# create an instance of InlineResponse200480ResultData from a dict
inline_response200480_result_data_from_dict = InlineResponse200480ResultData.from_dict(inline_response200480_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



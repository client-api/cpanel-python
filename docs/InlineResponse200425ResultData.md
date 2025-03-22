# InlineResponse200425ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**InlineResponse200425ResultDataCertificate**](InlineResponse200425ResultDataCertificate.md) |  | [optional] 
**host** | **str** | The issuer&#39;s hostname. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200425_result_data import InlineResponse200425ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200425ResultData from a JSON string
inline_response200425_result_data_instance = InlineResponse200425ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200425ResultData.to_json())

# convert the object into a dict
inline_response200425_result_data_dict = inline_response200425_result_data_instance.to_dict()
# create an instance of InlineResponse200425ResultData from a dict
inline_response200425_result_data_from_dict = InlineResponse200425ResultData.from_dict(inline_response200425_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



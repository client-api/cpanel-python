# InlineResponse200228ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The background color of the button on the cPanel interface. | [optional] 
**display_name** | **str** | The identity provider&#39;s friendly name. cPanel &amp; WHM interfaces will display this value. | [optional] 
**documentation_url** | **str** | The public URL of the identity provider&#39;s implementation documentation. | [optional] 
**icon** | **str** | The icon file to display on the button in the cPanel login interface. | [optional] 
**icon_type** | **str** | The icon file&#39;s MIME type. | [optional] 
**label** | **str** | The text label of the login icon in the cPanel login interface. | [optional] 
**link** | **str** | link to the identity provider&#39;s configuration for the appropriate service on the system. | [optional] 
**provider_name** | **str** | The identity provider&#39;s system name. | [optional] 
**textcolor** | **str** | The color of the text label in the cPanel login interface. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200228_result_data import InlineResponse200228ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200228ResultData from a JSON string
inline_response200228_result_data_instance = InlineResponse200228ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200228ResultData.to_json())

# convert the object into a dict
inline_response200228_result_data_dict = inline_response200228_result_data_instance.to_dict()
# create an instance of InlineResponse200228ResultData from a dict
inline_response200228_result_data_from_dict = InlineResponse200228ResultData.from_dict(inline_response200228_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


